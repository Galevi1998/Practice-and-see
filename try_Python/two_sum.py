from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictonary_nums={}
        for i in range(len(nums)):
            if(nums[i] in dictonary_nums and nums[i]+nums[dictonary_nums.get(nums[i])]==target):
                if(i<dictonary_nums.get(nums[i])):
                    return [i,dictonary_nums.get(nums[i])]
                else:
                    return [dictonary_nums.get(nums[i]),i]
            dictonary_nums[nums[i]] = i
    
def main():
    sol = Solution()
    nums = [0,4,3,0]

    print("Original list:", nums)

    k = sol.twoSum(nums,0)
    
    print("Number of unique elements:", k)

if __name__ == "__main__":
    main()