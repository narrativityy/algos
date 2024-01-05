/*

https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

*/

/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let answer = s
    const vowels = ['a', 'e', 'i', 'o', 'u']
    let strVowels = []
    let vowelsInd = []

    for (let i = 0; i < s.length; i++) {
        if (vowels.includes(s[i].toLowerCase())) {
            strVowels.push(s[i])
            vowelsInd.push(i)
        }
    }

    strVowels.reverse()

    for (let i = 0; i < vowelsInd.length; i++) {
        answer = answer.substring(0, vowelsInd[i]) + strVowels[i] + answer.substring(vowelsInd[i] + 1)
    }

    return answer
};

console.log(reverseVowels('hello'))