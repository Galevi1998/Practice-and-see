from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root=root.right,val=val)
        else:
            return self.searchBST(root=root.left,val=val)

        # solution for not binary tree
        # if root is None:
        #     return None
        # if root.val == val:
        #     return root
        # valLeft = self.searchBST(root=root.left,val=val)
        # if valLeft:
        #     return valLeft
        # valRight = self.searchBST(root=root.right,val=val)
        # if valRight:
        #     return valRight
        # return None
        


# ===== Helpers =====

def build_tree(level_order):
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


def tree_to_list(root):
    """Convert subtree to level-order list (trim trailing None)."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # remove trailing None
    while result and result[-1] is None:
        result.pop()

    return result


def run_test(tree_input, val, expected_subtree, test_name):
    sol = Solution()
    root = build_tree(tree_input)
    result = sol.searchBST(root, val)

    result_list = tree_to_list(result)
    if result_list == expected_subtree:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   tree_input:", tree_input)
        print("   val       :", val)
        print("   expected  :", expected_subtree)
        print("   got       :", result_list)


def main():
    tests = [

        # 🔹 Basic case
        (
            [4,2,7,1,3],
            2,
            [2,1,3],
            "basic_found"
        ),

        # 🔹 Not found
        (
            [4,2,7,1,3],
            5,
            [],
            "not_found"
        ),

        # 🔹 Root match
        (
            [4,2,7,1,3],
            4,
            [4,2,7,1,3],
            "root_match"
        ),

        # 🔹 Leaf node
        (
            [4,2,7,1,3],
            1,
            [1],
            "leaf_match"
        ),

        # 🔹 Right-heavy BST
        (
            [1,None,2,None,3,None,4],
            3,
            [3,None,4],
            "right_skewed"
        ),

        # 🔹 Left-heavy BST
        (
            [4,3,None,2,None,1],
            2,
            [2,1],
            "left_skewed"
        ),

        # 🔹 Single node found
        (
            [1],
            1,
            [1],
            "single_node_found"
        ),

        # 🔹 Single node not found
        (
            [1],
            2,
            [],
            "single_node_not_found"
        ),

        # 🔹 Empty tree
        (
            [],
            1,
            [],
            "empty_tree"
        ),

    ]

    for tree_input, val, expected, name in tests:
        run_test(tree_input, val, expected, name)


if __name__ == "__main__":
    main()
