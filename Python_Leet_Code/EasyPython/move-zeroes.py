from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nzeros = 0
        i=0
        # print(nums)
        while i < len(nums) :
            if nums[i] != 0:
                nums[i],nums[i-nzeros] = nums[i-nzeros] , nums[i]
            else:
                nzeros+=1
            i+=1


def run_test(sol: Solution, nums: List[int], expected: List[int], name: str) -> None:
    try:
        original_id = id(nums)
        sol.moveZeroes(nums)

        # בדיקה שזה באמת in-place
        same_object = id(nums) == original_id

        if nums == expected and same_object:
            print(f"✅ PASS: {name}")
        else:
            print(f"❌ FAIL: {name}")
            print(f"   expected = {expected}")
            print(f"   got      = {nums}")
            if not same_object:
                print("   ⚠️ Not in-place (array reference changed)")
    except NotImplementedError:
        print("🛑 NotImplementedError: Implement moveZeroes ואז תריץ שוב.")
        raise
    except Exception as e:
        print(f"💥 EXCEPTION: {name} → {type(e).__name__}: {e}")


def main():
    sol = Solution()

    tests = [
        # official example
        ([0,1,0,3,12], [1,3,12,0,0], "basic_example"),

        # no zeros
        ([1,2,3], [1,2,3], "no_zeros"),

        # all zeros
        ([0,0,0], [0,0,0], "all_zeros"),

        # zeros at start
        ([0,0,1], [1,0,0], "zeros_at_start"),

        # zeros at end
        ([1,2,0,0], [1,2,0,0], "zeros_at_end"),

        # single element
        ([0], [0], "single_zero"),
        ([5], [5], "single_non_zero"),

        # mixed
        ([4,0,5,0,0,3,0,1], [4,5,3,1,0,0,0,0], "complex_case"),

        # alternating
        ([0,1,0,2,0,3], [1,2,3,0,0,0], "alternating"),

        # negative numbers
        ([0,-1,0,-2], [-1,-2,0,0], "with_negatives"),
    ]

    for nums, expected, name in tests:
        run_test(sol, nums, expected, name)

    print("\nDone.")


if __name__ == "__main__":
    main()
