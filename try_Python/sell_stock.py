from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=0
        amount=0
        for i in range(1,len(prices)):
            if(prices[i]<prices[mini]):
                mini = i
            elif(prices[i]-prices[mini]>amount):
                amount = prices[i]-prices[mini]
        return amount

        
    
def main():
    sol = Solution()
    nums = [3,2,6,5,0,3]

    print("Original list:", nums)

    k = sol.maxProfit(nums)
    
    print("Number of unique elements:", k)

if __name__ == "__main__":
    main()