/*

https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let majorityNum = nums.length / 2
    let freqTable = {}
    for (num of nums) {
        if (freqTable[num] === undefined) {
            freqTable[num] = 1
            if (freqTable[num] > majorityNum) {
                return num
            }
        }
        else {
            freqTable[num]++
            if (freqTable[num] > majorityNum) {
                return num
            }
        }
    }

    return
};

console.log(majorityElement([3,2,3]))
console.log(majorityElement([2,2,1,1,1,2,2]))