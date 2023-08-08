# 🔴 Two Sum 🔴

## Level: Easy 🟩

🔹Problem🔹
---------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



🔹Related Topics🔹
---------------------------------------------------------------------------------
    Array
    Hash Table

🔹Idea🔹
---------------------------------------------------------------------------------
Essentially difference will be a copy of nums except put in a map data structure. The key is equal to 
nums[i] and the value is i. Now iterate over nums and check if the difference, target-nums[i], is in 
the map difference. If it is then return the current i and the value of differnce[target-nums[i]]. 

🔹Solution🔹
---------------------------------------------------------------------------------
    (1) create a map called difference
    (2) iterate over nums
        (i) check if target - nums[i]  in difference
            (a) if yes, return the indices
            (b) if no, add nums[i] to difference (aka difference[nums[i]] =  i)
🔹Run-Time🔹
---------------------------------------------------------------------------------
O(n) because the map has insertion/lookup time of O(1) and the worst case would be to iterate over the entire
list.