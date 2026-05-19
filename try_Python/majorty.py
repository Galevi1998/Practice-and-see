from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=0
        count=0
        for i in nums:
            if count>=len(nums):
                return candidate
            if count==0:
                candidate=i
            elif candidate == i:
                count+=1
            else:
                count-=1
        return candidate
        

def main():
    sol = Solution()
    nums = [4]
    print("Original list:", nums)

    k = sol.majorityElement(nums)
    
    print("Number of plusone elements:", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            