from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicton={}
        for i in nums:
            if i in dicton:
                dicton.update({i:dicton.get(i)+1})
            else:
                dicton[i]=1
        for i in nums:
            if dicton.get(i) == 1:
                return i
        

def main():
    sol = Solution()
    nums = [4]
    print("Original list:", nums)

    k = sol.singleNumber(nums)
    
    print("Number of plusone elements:", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            