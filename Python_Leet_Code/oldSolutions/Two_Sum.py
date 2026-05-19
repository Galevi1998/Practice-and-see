from typing import List


class Solution:
    def TwoSum(self, digits: List[int],target:int) -> List[int]:
        my_dict = {}
        for idx , i in enumerate(digits):
            if i in my_dict:
                return [my_dict[i], idx]
            else:
                my_dict[target - i] = idx


        

def main():
    sol = Solution()
    nums = [3,3]
    target = 6
    print("Original list:", nums)

    k = sol.TwoSum(nums,target)
    
    print("Number of plusone elements:", k)

if __name__ == "__main__":
    main()

            