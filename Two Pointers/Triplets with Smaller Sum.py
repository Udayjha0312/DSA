# Problem - Given an array arr[] of distinct integers and a value sum, find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.
# Approach - Two Pointers.
# Time Complexity - O(n^2)
# Space Complexity - Auxilary space is O(1) excluding O(k) output space.
class Solution:
    def countTriplets(self, target, arr):
        arr.sort()
        n = len(arr)
        count = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count

arr = [-2, 0, 1, 3]
target = 2

sol = Solution()
print(sol.countTriplets(target, arr))
                     

                 
