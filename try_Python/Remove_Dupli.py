from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0 
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1

def main():
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("Original list:", nums)

    k = sol.removeDuplicates(nums)
    
    print("Number of unique elements:", k)
    print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()
