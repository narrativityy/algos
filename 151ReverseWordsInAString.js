/* 

https://leetcode.com/problems/reverse-words-in-a-string/description/

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

*/
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let answerArr = s.split(" ")
    let answerStr = ''

    for (let i = answerArr.length - 1; i >= 0; i--) {
        if (answerArr[i] == '') {
            continue
        }
        answerStr += `${answerArr[i]} `
    }
    answerStr = answerStr.slice(0, answerStr.length - 1)

    return answerStr
};

console.log(reverseWords("the sky is blue"))