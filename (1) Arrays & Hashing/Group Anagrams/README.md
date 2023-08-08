# 🔴 Group Anagrams 🔴

## Level: Medium 🟧

🔹Problem🔹
---------------------------------------------------------------------------------
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.



🔹Related Topics🔹
---------------------------------------------------------------------------------
    Array
    Hash Table
    String
    Sorting

🔹Idea🔹
---------------------------------------------------------------------------------
For this problem the idea is to use unicode values of the characters for the words. For example,
"cat" and "ate" have the same unicode value. From this you can use a map to list anagrams together.
Then return ONLY the values of the map.

🔹Solution🔹
---------------------------------------------------------------------------------
(1) create a map called result
(2) for each word in strs
(3) create a list of size 26 (aka a .. z) called count
    (a) for each character in word
        (i) count[ord(character) - ord("a")] += 1
    (b) make count a tuple because a list cannot be a key for a map (note: tuples are immutable)
    (c) check if this specific count exists or not in result
        (i) yes it exists: result[count].append(word)
        (ii) does not exist: result[cound] = [word]

(4) return results

🔹Run-Time🔹
---------------------------------------------------------------------------------
O(m*n) such that m is the length of the array str and n is the average length word