/*

https //eetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let charSet = new Set()
    let l = 0
    let max = 0

    for (let r = 0; r < s.length; r++) {
        while (charSet.has(s[r])) {
            charSet.delete(s[l])
            l += 1
        }
        charSet.add(s[r])
        max = Math.max(max, charSet.size)
    }

    return max
};

console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))

/**
 * Version 1 slow algorithm
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstringSlow = function(s) {
    if (s.length < 1) {
        return 0
    }

    let l = 0
    let r = 1
    let max = 1

    let length = 1
    let curr = [s[l]]
    while (r < s.length) {
        if (!curr.includes(s[r])) {
            length += 1
            max = Math.max(max, length)
            curr.push(s[r])
            r += 1
        }
        else {
            length = 1
            l += 1
            r = l + 1
            curr = [s[l]]
        }
    }

    return max
};

// console.log(lengthOfLongestSubstringSlow("abcabcbb"))
// console.log(lengthOfLongestSubstringSlow("bbbbb"))
// console.log(lengthOfLongestSubstringSlow("pwwkew"))
