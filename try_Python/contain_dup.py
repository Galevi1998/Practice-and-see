from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
       arrow = "->"
       setush = set()
       for i in nums:
           if i not in setush :
               
    #    return ["e","dsf"]
    #    for i in nums:
           
            

            
            
        
        

def main():
    sol = Solution()
    nums = [0,1,2,4,5,7]
    print("Original list:", nums)

    k = sol.summaryRanges(nums)
    
    print("Number of plusone elements:", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            