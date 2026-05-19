from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str,digits)))
        num+=1
        numstr = str(num)
        x = []
        for i in numstr:
            x.append(int(i))
        return x
        

def main():
    sol = Solution()
    nums = [9,9,9,9,9]
    print("Original list:", nums)

    k = sol.plusOne(nums)
    
    print("Number of plusone elements:", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()

            