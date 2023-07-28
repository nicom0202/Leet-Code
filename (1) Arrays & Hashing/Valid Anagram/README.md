# 🔴 Valid Anagram 🔴

## Level: Easy 🟩

🔹Problem🔹
---------------------------------------------------------------------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.



🔹Related Topics🔹
---------------------------------------------------------------------------------
Array
Hash Table
Sorting

🔹Idea🔹
---------------------------------------------------------------------------------
    (1) Use a hash table with a size of 25 to represent the letters a-z
    (2) Add 1 for string1 and minus 1 for string2 for each letter

🔹Solution🔹
---------------------------------------------------------------------------------

(1) create a list of size 26 named letters(index 0 representing 'a' and index 25 representing 'z')

(2) iterate over string1 and string2 (assuming at this point they are the same size)
    (a) string1[i]++
    (b) string2[i]--

(3) iterate over letters to make sure each index has value 0 (aka it's an anagram)