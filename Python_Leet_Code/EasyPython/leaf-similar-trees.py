from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if root1.left is None and root2 : 
        #     return self.leafSimilar(root1=root1)==self.leafSimilar(root2=root2.left)
        # if root2.left is None and root1 : 
        #     return self.leafSimilar(root1=root1.left)==self.leafSimilar(root2=root2)
        # if root1.right is None and root2 : 
        #     return self.leafSimilar(root1=root1)==self.leafSimilar(root2=root2.right)
        # if root2.right is None and root1 : 
        #     return self.leafSimilar(root1=root1.right)==self.leafSimilar(root2=root2)
        if root1.left is None and root1.right and root2.left is None and root2.right : 
            print (root1.val,root2.val)
            return
        return (self.leafSimilar(root1=root1.left,root2=root2.left) and self.leafSimilar(root1=root1.right,root2=root2.right))
        


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


def run_test(tree1, tree2, expected, test_name):
    sol = Solution()
    root1 = build_tree(tree1)
    root2 = build_tree(tree2)
    result = sol.leafSimilar(root1, root2)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   tree1    :", tree1)
        print("   tree2    :", tree2)
        print("   expected :", expected)
        print("   got      :", result)


def main():
    tests = [

        # 🔹 Example-style: same leaf sequence
        (
            [3,5,1,6,2,9,8,None,None,7,4],
            [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8],
            True,
            "same_leaf_sequence"
        ),

        # 🔹 Different leaf sequences (same values but different order)
        (
            [1,2,3],   # leaves: [2,3]
            [1,3,2],   # leaves: [3,2]
            False,
            "same_values_diff_order"
        ),

        # 🔹 One tree is a single node
        (
            [1],       # leaves: [1]
            [1, None, 1],  # leaves: [1] (right leaf)
            True,
            "single_node_vs_tree_leaf"
        ),

        # 🔹 One empty tree, one non-empty
        (
            [],
            [1],
            False,
            "empty_vs_non_empty"
        ),

        # 🔹 Both empty (technically leaf sequences equal: [])
        (
            [],
            [],
            True,
            "both_empty"
        ),

        # 🔹 Same leaf sequence with very different structure
        (
            [1,2,None,3,None,4,None],  # chain left: leaves [4]
            [1,None,2,None,3,None,4],  # chain right: leaves [4]
            True,
            "different_structure_same_leaf"
        ),

        # 🔹 Duplicate leaf values, still must match multiplicity and order
        (
            [1,2,3,4,5,4,5],  # leaves: [4,5,4,5]
            [9,4,5,4,5],      # leaves: [4,5,4,5]
            True,
            "duplicates_match"
        ),

        # 🔹 Duplicate leaf values but different multiplicity
        (
            [1,2,3,4,4,4,4],  # leaves: [4,4,4,4]
            [1,2,3,4,4],      # leaves: [4,4]
            False,
            "duplicates_mismatch_count"
        ),

    ]

    for t1, t2, expected, name in tests:
        run_test(t1, t2, expected, name)


if __name__ == "__main__":
    main()
