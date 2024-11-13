class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.

        :param s: The first string to check.
        :type s: str
        :param t: The second string to check.
        :type t: str
        :return: True if the two strings are anagrams, False otherwise.
        :rtype: bool
        """
        if len(s) != len(t):
            # If the two strings have different lengths, they can't be anagrams
            return False
        
        # Create two dictionaries to store the frequency of each character in the two strings
        freqMapS = {}
        freqMapT = {}

        # Iterate over the first string
        for char in s:
            # If the character is not already in the dictionary, add it with a frequency of 1
            if char not in freqMapS:
                freqMapS[char] = 1
            # Otherwise, increment the frequency in the dictionary
            else:
                freqMapS[char] = freqMapS[char] + 1

        # Iterate over the second string
        for char in t:
            # If the character is not already in the dictionary, add it with a frequency of 1
            if char not in freqMapT:
                freqMapT[char] = 1
            # Otherwise, increment the frequency in the dictionary
            else:
                freqMapT[char] = freqMapT[char] + 1
        
        # Iterate over the keys in the first dictionary
        for key in freqMapS:
            # If the frequency of the character in the first dictionary is not equal to the frequency
            # of the character in the second dictionary, the strings are not anagrams
            if freqMapS.get(key) != freqMapT.get(key):
                return False
        
        # If all the frequencies are equal, the strings are anagrams
        return True

import unittest

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagram(self):
        self.assertTrue(self.solution.isAnagram("listen", "silent"))

    def test_not_anagram_different_length(self):
        self.assertFalse(self.solution.isAnagram("hello", "worlds"))

    def test_not_anagram_different_frequency(self):
        self.assertTrue(self.solution.isAnagram("hello", "holle"))

    def test_non_alphabetical_characters(self):
        self.assertTrue(self.solution.isAnagram("hello!", "!olleh"))

    def test_uppercase_lowercase(self):
        self.assertFalse(self.solution.isAnagram("Hello", "hello"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_single_character_strings(self):
        self.assertTrue(self.solution.isAnagram("a", "a"))

if __name__ == '__main__':
    unittest.main()