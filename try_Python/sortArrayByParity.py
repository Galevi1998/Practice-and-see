from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        indexOdd =1
        indexEven=0
        numLen = len(nums)
        while(indexOdd<numLen and indexEven<numLen):
            if(nums[indexEven]%2!=0 and nums[indexOdd]%2==0):
                helper = nums[indexEven]
                nums[indexEven] = nums[indexOdd]
                nums[indexOdd] = helper
            if(nums[indexEven]%2==0):
                indexEven= indexEven+2
            else:
                indexOdd = indexOdd+2
        return nums
        

def main():
    sol = Solution()
    nums = [648,831,560,986,192,997,424,829,897,843]
    print("", nums)

    k = sol.sortArrayByParityII(nums)
    
    print("", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            