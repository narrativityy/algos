/*

https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

*/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    if (height.length <= 1) {
        return 0
    }
    else if (height.length === 2) {
        return height[0] > height[1] ? height[1] : height[0]
    }

    let max = 0
    let maxInd = 0

    let maxHeight = 0

    for (let i = 0; i < height.length; i++) {
        if (height[i] > max) {
            max = height[i]
            maxInd = i
            for (let j = maxInd + 1; j < height.length; j++) {
                if (max < height[j]) {
                    if (max * (j - i) > maxHeight) {
                        maxHeight = max * (j - i)
                    }
                }
                else {
                    if (height[j] * (j - i) > maxHeight) {
                        maxHeight = height[j] * (j - i)
                    }
                }
            }
        }
    }



    return maxHeight
};

console.log(maxArea([1,8,6,2,5,4,8,3,7]))
console.log(maxArea([1,1]))