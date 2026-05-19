from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictUniqe = {}
        for i in arr :
            value = dictUniqe.get(i)
            if value is None:
                dictUniqe[i] = 1
            else:
                dictUniqe[i] = value+1

        values_set = set(dictUniqe.values())
        return len(dictUniqe) == len(values_set)


def run_test(arr, expected, test_name):
    sol = Solution()
    result = sol.uniqueOccurrences(arr)

    if result == expected:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
        print("   arr     :", arr)
        print("   expected:", expected)
        print("   got     :", result)


def main():
    tests = [

        # 🔹 Basic true
        ([1,2,2,1,1,3], True, "basic_true"),

        # 🔹 Basic false
        ([1,2], False, "basic_false"),

        # 🔹 All same number
        ([5,5,5,5], True, "all_same"),

        # 🔹 All unique numbers
        ([1,2,3,4], False, "all_unique_once"),

        # 🔹 Negative numbers
        ([-1,-1,-2,-2,-2,-3], True, "negative_numbers_true"),

        # 🔹 Negative numbers false
        ([-1,-1,-2,-2,-3,-3], False, "negative_numbers_false"),

        # 🔹 Single element
        ([7], True, "single_element"),

        # 🔹 Two numbers same frequency
        ([1,1,2,2], False, "two_same_frequency"),

        # 🔹 Multiple unique frequencies
        ([1,1,1,2,2,3], True, "multiple_unique_frequencies"),

        # 🔹 Large duplicates
        ([10]*5 + [20]*3 + [30]*2 + [40], True, "large_counts_unique"),

        # 🔹 Edge: empty array (LeetCode לא נותן, אבל חשוב לבדיקה מקומית)
        ([], True, "empty_array"),

    ]

    for arr, expected, name in tests:
        run_test(arr, expected, name)


if __name__ == "__main__":
    main()
