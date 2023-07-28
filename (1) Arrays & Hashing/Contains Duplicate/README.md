# 🔴 Contains Duplicate 🔴

## Level: Easy 🟩

🔹Problem🔹
---------------------------------------------------------------------------------
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


🔹Related Topics🔹
---------------------------------------------------------------------------------
Array
Hash Table
Sorting

🔹Idea🔹
---------------------------------------------------------------------------------
    (1) Want a data structure that has quick lookup time to check if the item exists already
    (2) Can be done in O(n) time because if every element is unique then all elements are looked at

🔹Solution🔹
---------------------------------------------------------------------------------
Create a set() in python.
Iterate over all elements. 
    (a) if element is in set(), return true
    (b) else, insert element in set

return false