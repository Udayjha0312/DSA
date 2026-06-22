# Problem - Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Approach - Two Pointers.
# Time Complexity - O(n^2)
# Space Complexity - Auxilary space is O(1) excluding O(k) output space.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for current in range(n - 2):
            if current > 0 and nums[current] == nums[current - 1]:
                continue

            left = current + 1
            right = n - 1

            while left < right:
                total = nums[current] + nums[left] + nums[right]

                if total == 0:
                    result.append(
                        [nums[current], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


nums = [-3, -2, -1, 0, 1, 2, 3]
sol = Solution()
print(sol.threeSum(nums))
                        
                     
                     
           

                
                

                

                  





