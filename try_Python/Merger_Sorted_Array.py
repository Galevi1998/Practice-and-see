
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num1Len = len(nums1)-1
        while(m>0 and n>0):
            if(nums1[m-1]<nums2[n-1]):
                print("before1 change",nums1)
                nums1[num1Len] = nums2[n-1]
                n-=1
                num1Len-=1
                print("after1 change",nums1)

            else:
                print("before change",nums1)
                nums1[num1Len]=nums1[m-1]
                nums1[m-1]=0
                m-=1
                num1Len-=1
                print("after change",nums1)

        if(n>0):
            nums1[:n] = nums2[:n]
            
        

def main():
    sol = Solution()
    num1 = [1,2,3,0,0,0]
    num2 = [1,2,6]


    print("Original list:", num1)
    print("Original list:", num2)


    sol.merge(num1,3,num2,3)
    
    print("Number of unique elements:", num1)

if __name__ == "__main__":
    main()