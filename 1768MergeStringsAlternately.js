/*

https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

*/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let lowerLength
    let higherLength
    if (word1.length < word2.length) {
        lowerLength = word1.length
        higherLength = word2.length
    }
    else {
        lowerLength = word2.length
        higherLength = word1.length
    }
    let mergedStr = ""
    let i = 0
    for (i; i < lowerLength; i++) {
        mergedStr += word1[i]
        mergedStr += word2[i]
    }
    if (i >= word1.length) {
        for (i; i < higherLength; i++) {
            mergedStr += word2[i]
        }
    }
    else {
        for (i; i < higherLength; i++) {
            mergedStr += word1[i]
        }
    }
    return mergedStr
};

console.log(mergeAlternately("abc", "pqr"))