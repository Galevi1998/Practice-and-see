from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums :
            if i in my_dict:
                return True
            my_dict[i] = i
        return False


def main():
    sol = Solution()

    # דוגמאות לבדיקה
    test_cases = [
        ([1, 2, 3, 1], True),   # יש כפילות
        ([1, 2, 3, 4], False),  # אין כפילות
        ([1,1,1,3,3,4,3,2,4,2], True), # הרבה כפילויות
        ([], False),            # רשימה ריקה
    ]

    for nums, expected in test_cases:
        result = sol.containsDuplicate(nums)
        print(f"Input: {nums} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    main()
