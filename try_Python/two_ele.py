from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        
        return end + 1  # New length of array with val removed

    
def main():
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]

    print("Original list:", nums)

    k = sol.removeElement(nums,2)
    
    print("Number of unique elements:", k)
    print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()