from typing import List
import statistics


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxEverege = sum(nums[:k])
        window = maxEverege
        i=1
        lenNums = len(nums)
        for i in range(1, lenNums - k + 1) : 
            window = window-nums[i-1]+nums[i+k-1]
            if window > maxEverege : 
                maxEverege = window
        return maxEverege/k
    
    


def approx_equal(a: float, b: float, eps: float = 1e-5) -> bool:
    return abs(a - b) <= eps


def run_test(sol: Solution, nums: List[int], k: int, expected: float, name: str) -> None:
    try:
        got = sol.findMaxAverage(nums, k)
        if approx_equal(got, expected):
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   nums     = {nums}")
            print(f"   k        = {k}")
            print(f"   expected = {expected}")
            print(f"   got      = {got}")
            print(f"   diff     = {abs(got - expected)}")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement findMaxAverage ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official-style examples
        ([1, 12, -5, -6, 50, 3], 4, 12.75, "example_1"),
        ([5], 1, 5.0, "single_element"),

        # all negatives
        ([-1, -12, -5, -6], 2, -5.5, "all_negative"),

        # mixed, k=1 => max element
        ([0, -1, 2, 3, -5], 1, 3.0, "k_equals_1"),

        # k == n => whole array average
        ([2, 2, 2, 2], 4, 2.0, "k_equals_n"),

        # repeated max windows
        ([1, 2, 3, 4, 5], 2, 4.5, "increasing"),
        ([5, 4, 3, 2, 1], 2, 4.5, "decreasing"),

        # zeros and negatives
        ([0, 0, 0, 0], 2, 0.0, "all_zeros"),
        ([0, -1, 0, -1, 0], 3, -1/3, "zeros_and_negatives"),

        # tricky: large values
        ([10000, -10000, 10000, -10000, 10000], 2, 0.0, "alternating_large"),
        
    ]

    for nums, k, expected, name in tests:
        run_test(sol, nums, k, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
