package leet_code_java;

import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] twoArr = new int[2];
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        int indexStart = 0;
        int indexEnd = nums.length-1;
        while (indexEnd!=indexStart) {
            if(nums[indexEnd]+nums[indexStart]<target){
                indexStart++;
            }
            if (nums[indexEnd]+nums[indexStart]>target) {
                indexEnd--;
            }
            if(nums[indexEnd]+nums[indexStart]==target){
                twoArr[0]=indexStart;
                twoArr[1]=indexEnd;
                return twoArr;
            }
        } 
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {3,2,4};
        int target = 6;
        System.out.println(nums);

        int[] result = sol.twoSum(nums, target);

        if (result != null) {
            System.out.println("Indices: " + Arrays.toString(result));
        } else {
            System.out.println("No solution found.");
        }
    }
}
