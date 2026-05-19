from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = prices[0]
        lowest = prices[0]
        for i in range(len(prices)):
            if
        

def main():
    sol = Solution()
    nums = [7,1,5,3,6,4]
    print("Original list:", nums)

    k = sol.maxProfit(nums)
    
    print("Number of unique elements:", k)
    print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()
