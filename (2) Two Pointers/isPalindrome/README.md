# 🔴 isPalindrome 🔴

## Level: Easy 🟩

🔹Problem🔹
---------------------------------------------------------------------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


🔹Related Topics🔹
---------------------------------------------------------------------------------
Two Pointer
String

🔹Idea🔹
---------------------------------------------------------------------------------
    (1) Have two pointers. One pointer at the front of the string & one at the end of the string
    (2) Check that the pointers point to the same character and move them toward the middle

🔹Solution🔹
---------------------------------------------------------------------------------
Check base cases of size 0 and 1 (always true)
Have two pointers, front & back
while front < back:
    skip if front is not alphanum & move the pointer up one
    skip if back is not alphanum & move the pointer down one
    check if the chars at position front & back are the same
    if not the same, return false
return true

🔹Run-Time🔹
---------------------------------------------------------------------------------
O(n)
Why? - If the string is a palindrome then we will check all n characters 