from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNum1 = set(nums1)
        setNum2 = set(nums2)
        lstReturn = []
        for i in nums1 :
            if i in setNum2:
                setNum1.remove(i)
                setNum2.remove(i)
        return [list(setNum1),list(setNum2)]


def normalize(result: List[List[int]]) -> List[List[int]]:
    """
    Normalize output for comparison:
    - remove duplicates
    - sort inner lists
    - sort outer structure
    """
    return sorted([sorted(list(set(lst))) for lst in result])


def run_test(nums1, nums2, expected, test_name):
    sol = Solution()
    result = sol.findDifference(nums1, nums2)

    if normalize(result) == normalize(expected):
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   nums1:", nums1)
        print("   nums2:", nums2)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic example
        ([1,2,3], [2,4,6], [[1,3],[4,6]], "basic_case"),

        # 🔹 Duplicates in both arrays
        ([1,2,2,3,3], [2,2,4], [[1,3],[4]], "duplicates_case"),

        # 🔹 Identical arrays
        ([1,2,3], [1,2,3], [[],[]], "identical_arrays"),

        # 🔹 One empty
        ([], [1,2,3], [[],[1,2,3]], "nums1_empty"),

        # 🔹 Other empty
        ([1,2,3], [], [[1,2,3],[]], "nums2_empty"),

        # 🔹 Both empty
        ([], [], [[],[]], "both_empty"),

        # 🔹 Negative numbers
        ([-1,-2,3], [-2,4], [[-1,3],[4]], "negative_numbers"),

        # 🔹 Large duplicates only
        ([5,5,5,5], [5,5], [[],[]], "all_duplicates_same_value"),

        # 🔹 Completely disjoint
        ([1,3,5], [2,4,6], [[1,3,5],[2,4,6]], "disjoint_arrays"),

        # 🔹 Overlap but asymmetric sizes
        ([1,2,3,4,5], [3,4], [[1,2,5],[]], "partial_overlap"),

        # 🔹 Single element different
        ([1], [2], [[1],[2]], "single_element_diff"),

        # 🔹 Single element same
        ([7], [7], [[],[]], "single_element_same"),

    ]

    for nums1, nums2, expected, name in tests:
        run_test(nums1, nums2, expected, name)


if __name__ == "__main__":
    main()
