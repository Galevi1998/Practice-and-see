from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            print(root.val)
            return 1
        if root.left is None and root.right:
            # print(root.val)
            return self.maxDepth(root.right)+1
        if root.right is None and root.left is not None:
            # print(root.val)
            return self.maxDepth(root.left)+1
        print(root.val)
        return max(self.maxDepth(root.left)+1 , self.maxDepth(root.right)+1)


# ===== Helpers =====

def build_tree(level_order):
    """
    Builds tree from level-order list (LeetCode style).
    None represents missing node.
    """
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


def run_test(tree_input, expected, test_name):
    sol = Solution()
    root = build_tree(tree_input)
    result = sol.maxDepth(root)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   tree_input:", tree_input)
        print("   expected  :", expected)
        print("   got       :", result)


def main():
    tests = [

        # 🔹 Basic example
        ([3,9,20,None,None,15,7], 3, "basic_example"),

        # 🔹 Single node
        ([1], 1, "single_node"),

        # 🔹 Empty tree
        ([], 0, "empty_tree"),

        # 🔹 Left skewed
        ([1,2,None,3,None,4,None], 4, "left_skewed"),

        # 🔹 Right skewed
        ([1,None,2,None,3,None,4], 4, "right_skewed"),

        # 🔹 Full balanced tree
        ([1,2,3,4,5,6,7], 3, "balanced_tree"),

        # 🔹 Deep uneven tree
        ([1,2,3,4,None,None,None,5], 4, "uneven_tree"),

        # 🔹 Only root with two null children
        ([1,None,None], 1, "root_with_null_children"),

    ]

    for tree_input, expected, name in tests:
        run_test(tree_input, expected, name)


if __name__ == "__main__":
    main()
