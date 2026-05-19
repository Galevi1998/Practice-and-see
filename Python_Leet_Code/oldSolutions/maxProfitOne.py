from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> List[int]:
        maxProf = 0
        min = max = prices[0]
        for i in prices :
            if i < min:
                min = max = i
            if i > max and i - min > maxProf:
                max = i
                maxProf = max - min
        return maxProf



        


        

def main():
    sol = Solution()
    prices = [7,1,5,0,6,0]
    print("Original list:", prices)

    k = sol.maxProfit(prices)
    
    print("Prices of plusone elements:", k)

if __name__ == "__main__":
    main()

            