from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if freq.get(i):
                freq[i] += 1
            else:
                freq[i] = 1
        
        # Sort based on (frequency ascending, number descending)
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums


def main():
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("Original list:", nums)

    k = sol.frequencySort(nums)
    
    print("Number of unique elements:", k)
    # print("Modified list with unique elements at the front:", nums[:k])

if __name__ == "__main__":
    main()
