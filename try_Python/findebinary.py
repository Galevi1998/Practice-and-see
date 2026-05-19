from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lstlen = len(nums)-1
        start=0
        while(start<=lstlen):
            middle=(lstlen+start)//2
            if(nums[middle]==target):
                return middle
            if(nums[middle]>target):
                print(nums[middle])
                print("here1")
                lstlen=middle-1
            else:
                print("here2")
                start=middle+1
            print (f"start - {start} end -{lstlen}")
            
        return start


def main():
    sol = Solution()
    nums = [1,3]
    print("Original list:", nums)

    k = sol.searchInsert(nums,8)
    
    print("Number of unique elements:", k)
    print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            