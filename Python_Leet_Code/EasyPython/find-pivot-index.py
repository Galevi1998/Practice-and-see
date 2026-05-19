from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        left = 0
        print(totalSum)
        for i in range(len(nums)) :
            print(totalSum - left -nums[i] , left)
            if totalSum - left -nums[i]  == left :
                return i
            left+=nums[i]
        return -1


def run_test(sol: Solution, nums: List[int], expected: int, name: str) -> None:
    try:
        got = sol.pivotIndex(nums)
        if got == expected:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   nums     = {nums}")
            print(f"   expected = {expected}")
            print(f"   got      = {got}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement pivotIndex ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official examples
        ([1, 7, 3, 6, 5, 6], 3, "example_1"),
        ([1, 2, 3], -1, "example_2"),
        ([2, 1, -1], 0, "example_3"),

        # single element
        ([10], 0, "single_element"),

        # pivot at start
        ([0, 1, -1], 0, "pivot_at_start"),

        # pivot at end
        ([1, -1, 0], 2, "pivot_at_end"),

        # multiple possible pivots → leftmost required
        ([0, 0, 0, 0], 0, "multiple_pivots"),

        # negatives
        ([-1, -1, -1, 0, 1, 1], 0, "negatives_case"),

        # no pivot
        ([5, 6, 7], -1, "no_pivot"),

        # larger mixed
        ([3, -2, 5, -1, 2, -2, 1], 2, "complex_case"),
    ]

    for nums, expected, name in tests:
        run_test(sol, nums, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
