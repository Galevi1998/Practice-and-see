from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        return 0
        #do it again bro

# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    print("Test case 1 result:", sol.maxArea(height1))  # Expected: 49

    # Test case 2
    height2 = [1,1]
    print("Test case 2 result:", sol.maxArea(height2))  # Expected: 2

    # Test case 3
    height3 = [4,3,2,1,4]
    print("Test case 3 result:", sol.maxArea(height3))  # Expected: 16

    # Test case 4
    height4 = [1,2,1]
    print("Test case 4 result:", sol.maxArea(height4))  # Expected: 2
