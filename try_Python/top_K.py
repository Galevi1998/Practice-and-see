from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary_count = {}
        for num in nums:
            dictionary_count[num] = dictionary_count.get(num, 0) + 1

        # Sort keys by their frequency, descending
        sorted_keys = sorted(dictionary_count, key=dictionary_count.get, reverse=True)
        
        return sorted_keys[:k]



        # for i in range(k):
        #     maxi = max(dictionary_count,key=dictionary_count.get)
        #     biggest.insert(i,maxi)
        #     dictionary_count.pop(maxi)
        # return biggest
        
def main():
    s = Solution()

    # Test case 1
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    print("Test 1:", s.topKFrequent(nums1, k1))  # Expected: [1, 2] (order can vary)

    # Test case 2
    nums2 = [1]
    k2 = 1
    print("Test 2:", s.topKFrequent(nums2, k2))  # Expected: [1]

    # Test case 3
    nums3 = [4,1,-1,2,-1,2,3]
    k3 = 2
    print("Test 3:", s.topKFrequent(nums3, k3))  # Expected: [-1, 2] or [2, -1]

if __name__ == "__main__":
    main()
