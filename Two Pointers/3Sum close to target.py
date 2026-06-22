# Problem - Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
            # Return the sum of the three integers.
# Approach - Two Pointers.
# Time Complexity - O(n^2)
# Space Complexity - Auxilary space is O(1) excluding O(k) output space.

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest


nums = [0,0,0]
target = 1

sol = Solution()
print(sol.threeSumClosest(nums, target))
            


             
            
