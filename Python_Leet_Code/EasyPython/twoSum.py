from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        for i in range(len(nums)) :
            num = nums[i]
            if num in targetDict:
                return [targetDict[num], i]
            targetDict[target-num] = i


    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)) :
            blockNum = nums[i]
            if blockNum in numsDict:
                return [numsDict[blockNum],i]
            numsDict[target - blockNum] = i    


def all_valid_pairs(nums: List[int], target: int):
    pairs = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                pairs.add((i, j))
    return pairs


def validate_two_sum_output(nums: List[int], target: int, out):
    assert isinstance(out, list), f"Expected list, got {type(out)}"
    assert len(out) == 2, f"Expected 2 indices, got {len(out)}"
    assert all(isinstance(x, int) for x in out), "Indices must be integers"

    i, j = out[0], out[1]
    assert i != j, "Indices must be different"
    assert 0 <= i < len(nums) and 0 <= j < len(nums), "Index out of range"
    assert nums[i] + nums[j] == target, "Returned indices do not sum to target"

    valid = all_valid_pairs(nums, target)
    # LeetCode Two Sum promises a solution; this check ensures we don't overfit order
    assert valid, "Test data should have at least one valid pair"
    a, b = (i, j) if i < j else (j, i)
    assert (a, b) in valid, "Returned pair is not a valid solution"


def run_test(name: str, nums: List[int], target: int):
    sol = Solution()
    out = sol.twoSum(nums, target)
    validate_two_sum_output(nums, target, out)
    print(f"✅ {name} passed -> output: {out}")


def main():
    tests = [
        ("basic_example", [2, 7, 11, 15], 9),
        ("unsorted_middle", [3, 2, 4], 6),
        ("duplicates", [3, 3], 6),
        ("negative_numbers", [-1, -2, -3, -4, -5], -8),  # -3 + -5
        ("mixed_signs", [-10, 7, 19, 3, 2], 9),          # 7 + 2
        ("zeros", [0, 4, 3, 0], 0),                      # 0 + 0
        ("larger_case", [1, 5, 1, 5, 9, 13, 7], 10),     # 1 + 9 or 5 + 5
    ]

    for name, nums, target in tests:
        run_test(name, nums, target)

    print("\n🎉 All test cases passed.")


if __name__ == "__main__":
    main()