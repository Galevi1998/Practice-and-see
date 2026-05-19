from typing import List

# Contains Duplicate - test harness
# You asked: don't fill Solution, only main + test cases.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for i in nums :
            if i in numsSet :
                return True
            else:
                numsSet.add(i)
        return False


def run_test(name: str, nums: List[int], expected: bool):
    sol = Solution()
    out = sol.containsDuplicate(nums)
    assert isinstance(out, bool), f"{name}: Expected bool, got {type(out)}"
    assert out == expected, f"{name}: Expected {expected}, got {out}"
    print(f"✅ {name} passed -> {out}")


def main():
    tests = [
        ("single_element", [1], False),
        ("two_unique", [1, 2], False),
        ("two_same", [7, 7], True),
        ("basic_true", [1, 2, 3, 1], True),
        ("basic_false", [1, 2, 3, 4], False),
        ("negatives_true", [-1, -2, -3, -1], True),
        ("zeros_true", [0, 0, 1], True),
        ("spread_duplicate", [10, 20, 30, 40, 10], True),
        ("sorted_unique", [1, 2, 3, 4, 5, 6], False),
        ("sorted_with_dup", [1, 1, 2, 3, 4], True),
        ("large_unique_range", list(range(1000)), False),
        ("large_with_one_dup", list(range(999)) + [500], True),
        # Extra edge-case robustness (not always in LC constraints)
        ("empty_list", [], False),
    ]

    for name, nums, expected in tests:
        run_test(name, nums, expected)

    print("\n🎉 All test cases passed.")


if __name__ == "__main__":
    main()
