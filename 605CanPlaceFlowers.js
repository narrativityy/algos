/*

https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

*/

/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let count = 0;
    if (n === 0) {
        return true
    }
    if (flowerbed.length === 1) {
        if (flowerbed[0] === 0) {
            return true
        }
        return false
    }
    for (let i = 0; i < flowerbed.length; i++) {
        if (i === 0) {
            if (flowerbed[i] === 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1
                count++
            }
        }
        else if (i === flowerbed.length - 1) {
            if (flowerbed[i - 1] === 0 && flowerbed[i] === 0) {
                flowerbed[i] = 1
                count++
            }
        }
        else {
            if (flowerbed[i - 1] === 0 && flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
                flowerbed[i] = 1
                count++
            }
        }
    }

    return count >= n
};

console.log(canPlaceFlowers([1,0,0,0,1], 1))