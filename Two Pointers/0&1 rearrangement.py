# Problem - Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
# Approach - Two Pointers.
# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution:
    def rearrange(self, arr):
        left = 0
        right = len(arr) - 1
        for left in range(0,len(arr)):
            while left < right:
                if arr[left]==0:
                    left+=1
                elif arr[left]==1:
                    arr[left],arr[right]=arr[right],arr[left]
                    right-=1
                else:
                    right-=1
        return arr

sol = Solution()
result = sol.rearrange([1,0,1,0,1,0])
print(result)



