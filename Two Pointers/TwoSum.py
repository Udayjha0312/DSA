# Problem - Given an array of integers nums and an integer target, return  the two numbers such that they add up to target.
# Approach -  Two Pointers 
# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return [left, right]
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return []







