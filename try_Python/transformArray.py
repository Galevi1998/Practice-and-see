from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # indexEnd =len(nums)-1
        # indexStart=0
        # while indexEnd>=indexStart :
        #     if nums[indexStart]%2==0:
        #         nums[indexStart] =0
        #         indexStart+=1
        #     elif nums[indexEnd]%2!=0:
        #         nums[indexEnd] =1
        #         indexEnd-=1
        #     else:
        #         nums[indexEnd]=1
        #         nums[indexStart]=0
        # return nums
        j =0 
        for i in nums:
            if i%2==0 :
                nums[j] =0
                j+=1
        for j in range(j,len(nums)):
            nums[j] = 1
        return nums



        

def main():
    sol = Solution()
    nums = [648,831,560,986,192,997,424,829,897,843]
    print("", nums)

    k = sol.transformArray(nums)
    
    print("", k)

if __name__ == "__main__":
    main()