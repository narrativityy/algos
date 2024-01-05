/*

https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

*/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let correctSeq = 0
    for (let i = 0; i < t.length; i++) {
        if (s[correctSeq] === t[i]) {
            correctSeq++
        }
    }

    return correctSeq === s.length
};

console.log(isSubsequence("abc", "ahbgdc"))
console.log(isSubsequence("axc", "ahbgdc"))