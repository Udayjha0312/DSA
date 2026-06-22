# Problem - Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Approach - Two Pointers.
# Time Complexity - O(n)
# Space Complexity - O(n)
class Solution:
    def sortedSquares(self, arr: list[int]) -> list[int]:
       n = len(arr)
       res = [0]*n
       left = 0
       right = n - 1
       k = n - 1
       while left<=right:
           if abs(arr[left])>abs(arr[right]):
               res[k]=arr[left]*arr[left]
               left+=1
           else:
               res[k]=arr[right]*arr[right]
               right-=1
           k-=1
       return res
    
arr = [-4,-1,0,3,10]
sol = Solution()
result = sol.sortedSquares(arr)
print(result)
               

           
        