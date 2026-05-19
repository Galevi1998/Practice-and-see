import argparse
import os
import numpy as np
import cv2
import torch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

from pointpillars.model import PointPillars
from pointpillars.utils import (
    read_points, read_calib, read_label,
    keep_bbox_from_image_range, keep_bbox_from_lidar_range,
    bbox_camera2lidar, bbox3d2corners_camera, points_camera2image
)

def point_range_filter(pts, point_range=[0, -39.68, -3, 69.12, 39.68, 1]):
    mask = (
        (pts[:, 0] > point_range[0]) & (pts[:, 0] < point_range[3]) &
        (pts[:, 1] > point_range[1]) & (pts[:, 1] < point_range[4]) &
        (pts[:, 2] > point_range[2]) & (pts[:, 2] < point_range[5])
    )
    return pts[mask]

def draw_rotated_box(ax, x, y, dx, dy, heading, color="r", linestyle="-"):
    c, s = np.cos(heading), np.sin(heading)
    R = np.array([[c, -s], [s, c]])
    corners = np.array([[dx/2, dy/2], [dx/2, -dy/2], [-dx/2, -dy/2], [-dx/2, dy/2]])
    rotated = corners @ R.T + np.array([x, y])
    ax.add_patch(plt.Polygon(rotated, fill=False, edgecolor=color, linewidth=2, linestyle=linestyle))

def vis_pc_colab_side_by_side(pc, frame_id, pred_bboxes=None, pred_labels=None, pred_scores=None,
                               gt_bboxes=None, gt_labels=None, save_path=None):
    class_names = ["Pedestrian", "Cyclist", "Car"]
    class_colors = {0: '#FF5733', 1: '#33FF57', 2: '#339CFF'}

    fig, axes = plt.subplots(1, 3, figsize=(24, 10), gridspec_kw={'width_ratios': [1, 1, 0.25]})
    titles = ["Prediction", "Ground Truth"]

    def draw_text_with_line(ax, x, y, text, color, index_offset):
        dy = 3.5 + index_offset * 1.8
        ax.add_line(mlines.Line2D([x, x], [y, y + dy], color=color, linewidth=1.0, alpha=0.9))
        ax.text(x, y + dy, text,
                fontsize=16, weight='bold', color='white',
                bbox=dict(facecolor=color, edgecolor='none', boxstyle="round,pad=0.4", alpha=0.95))

    for idx in range(2):
        ax = axes[idx]
        ax.set_facecolor('black')
        ax.set_title(f"{titles[idx]} – Frame {frame_id}", fontsize=18, color='white')
        ax.set_xlabel("X (m)", fontsize=12, color='white')
        ax.set_ylabel("Y (m)", fontsize=12, color='white')
        ax.set_aspect("equal")
        ax.tick_params(colors='white')
        ax.scatter(pc[:, 0], pc[:, 1], s=0.5, c="lightgray", alpha=0.6)

    if pred_bboxes is not None and pred_labels is not None:
        for i, box in enumerate(pred_bboxes):
            x, y, z, dx, dy, dz, heading = box
            label = pred_labels[i]
            score = pred_scores[i] if pred_scores is not None else 0.0
            color = class_colors.get(label, 'white')
            draw_rotated_box(axes[0], x, y, dx, dy, heading, color=color)
            draw_text_with_line(axes[0], x, y, f"{class_names[label]} {score * 100:.1f}%", color, i)

    if gt_bboxes is not None and gt_labels is not None:
        for i, box in enumerate(gt_bboxes):
            x, y, z, dx, dy, dz, heading = box
            label = gt_labels[i]
            color = class_colors.get(label, 'white')
            draw_rotated_box(axes[1], x, y, dx, dy, heading, color=color, linestyle='--')
            draw_text_with_line(axes[1], x, y, class_names[label], color, i)

    # Legend
    axes[2].axis('off')
    axes[2].set_facecolor('white')
    axes[2].set_title("Legend", fontsize=16)
    y_offset = 0.9
    for cls_id, cls_name in enumerate(class_names):
        axes[2].add_patch(mpatches.Rectangle((0.1, y_offset - 0.05), 0.1, 0.05, color=class_colors[cls_id]))
        axes[2].text(0.25, y_offset - 0.025, cls_name, fontsize=14, verticalalignment='center')
        y_offset -= 0.12

    plt.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=200, facecolor=fig.get_facecolor())
        print(f"📸 Saved updated visualization to {save_path}")
    else:
        plt.show()

def main(args):
    CLASSES = {'Pedestrian': 0, 'Cyclist': 1, 'Car': 2}
    pcd_limit_range = np.array([0, -40, -3, 70.4, 40, 0.0], dtype=np.float32)

    model = PointPillars(nclasses=len(CLASSES))
    model.load_state_dict(torch.load(args.ckpt, map_location='cuda' if not args.no_cuda else 'cpu'))
    model = model.cuda() if not args.no_cuda else model

    pc = point_range_filter(read_points(args.pc_path))
    pc_torch = torch.from_numpy(pc).cuda() if not args.no_cuda else torch.from_numpy(pc)

    calib_info = read_calib(args.calib_path) if args.calib_path and os.path.exists(args.calib_path) else None
    gt_label = read_label(args.gt_path) if args.gt_path and os.path.exists(args.gt_path) else None

    model.eval()
    with torch.no_grad():
        result_filter = model(batched_pts=[pc_torch], mode='test')[0]

    if calib_info:
        result_filter = keep_bbox_from_image_range(result_filter,
            calib_info['Tr_velo_to_cam'].astype(np.float32),
            calib_info['R0_rect'].astype(np.float32),
            calib_info['P2'].astype(np.float32),
            (375, 1242))

    result_filter = keep_bbox_from_lidar_range(result_filter, pcd_limit_range)

    # 🎯 Apply score threshold
    threshold = 0.7
    mask = result_filter['scores'] >= threshold
    lidar_bboxes = result_filter['lidar_bboxes'][mask]
    labels = result_filter['labels'][mask]
    scores = result_filter['scores'][mask]

    gt_lidar_bboxes = None
    gt_labels = None
    if calib_info and gt_label:
        try:
            dims, locs, rots = gt_label['dimensions'], gt_label['location'], gt_label['rotation_y']
            names = gt_label['name']
            raw_labels = np.array([CLASSES.get(n, -1) for n in names])
            sel = raw_labels != -1
            if sel.sum() > 0:
                gt_labels = raw_labels[sel]
                bboxes_camera = np.concatenate([locs, dims, rots[:, None]], axis=-1)[sel]
                gt_lidar_bboxes = bbox_camera2lidar(
                    bboxes_camera,
                    calib_info['Tr_velo_to_cam'],
                    calib_info['R0_rect']
                )
        except Exception as e:
            print("❌ Error parsing GT:", e)

    save_path = os.path.join(
        "/content/drive/MyDrive/kitti_output",
        os.path.basename(args.pc_path).replace(".bin", "_side_by_side.png")
    )
    vis_pc_colab_side_by_side(
        pc, os.path.basename(args.pc_path).replace(".bin", ""),
        pred_bboxes=lidar_bboxes,
        pred_labels=labels,
        pred_scores=scores,
        gt_bboxes=gt_lidar_bboxes,
        gt_labels=gt_labels,
        save_path=save_path
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PointPillars Inference & Visualization')
    parser.add_argument('--ckpt', required=True, help='Path to checkpoint .pth')
    parser.add_argument('--pc_path', required=True, help='Path to .bin point cloud file')
    parser.add_argument('--gt_path', default='', help='Ground truth label .txt file path')
    parser.add_argument('--calib_path', default='', help='Calibration file path')
    parser.add_argument('--img_path', default='', help='Optional image path')
    parser.add_argument('--no_cuda', action='store_true', help='Use CPU only')
    args = parser.parse_args()

    main(args)









#===================================================================================================
    


# This file is modified from https://github.com/open-mmlab/mmdetection3d/blob/master/mmdet3d/ops/voxel/voxelize.py

import torch
import torch.nn as nn
from pointpillars.ops.voxel_op import hard_voxelize  # Make sure this is properly defined and compiled

class _Voxelization(torch.autograd.Function):

    @staticmethod
    def forward(ctx,
                points,
                voxel_size,
                coors_range,
                max_points=35,
                max_voxels=20000,
                deterministic=True):
        """
        Convert raw point cloud into voxel tensors.
        """
        # 🔒 Fix: ensure the points tensor is contiguous in memory
        points = points.contiguous()

        voxels = points.new_zeros(
            size=(max_voxels, max_points, points.size(1)))
        coors = points.new_zeros(size=(max_voxels, 3), dtype=torch.int)
        num_points_per_voxel = points.new_zeros(size=(max_voxels,), dtype=torch.int)

        voxel_num = hard_voxelize(
            points, voxels, coors,
            num_points_per_voxel,
            voxel_size, coors_range,
            max_points, max_voxels, 3,
            deterministic
        )

        voxels_out = voxels[:voxel_num]
        coors_out = coors[:voxel_num].flip(-1)  # flip (z, y, x) -> (x, y, z)
        num_points_out = num_points_per_voxel[:voxel_num]
        return voxels_out, coors_out, num_points_out


class Voxelization(nn.Module):
    def __init__(self,
                 voxel_size,
                 point_cloud_range,
                 max_num_points,
                 max_voxels,
                 deterministic=True):
        super().__init__()
        self.voxel_size = voxel_size
        self.point_cloud_range = point_cloud_range
        self.max_num_points = max_num_points
        self.max_voxels = max_voxels
        self.deterministic = deterministic

        pc_range = torch.tensor(point_cloud_range, dtype=torch.float32)
        voxel_sz = torch.tensor(voxel_size, dtype=torch.float32)
        grid_size = torch.round((pc_range[3:] - pc_range[:3]) / voxel_sz).long()

        self.grid_size = grid_size
        input_feat_shape = grid_size[:2]
        self.pcd_shape = [*input_feat_shape, 1][::-1]  # [z, y, x]

    def forward(self, points):
        max_voxels = self.max_voxels[0] if self.training else self.max_voxels[1]
        return _Voxelization.apply(
            points, self.voxel_size, self.point_cloud_range,
            self.max_num_points, max_voxels, self.deterministic
        )

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"voxel_size={self.voxel_size}, "
                f"point_cloud_range={self.point_cloud_range}, "
                f"max_num_points={self.max_num_points}, "
                f"max_voxels={self.max_voxels}, "
                f"deterministic={self.deterministic})")
