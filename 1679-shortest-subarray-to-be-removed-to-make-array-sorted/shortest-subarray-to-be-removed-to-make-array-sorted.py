# class Solution:
#     def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
#         def binsearch(search,number):
#             left=0
#             right=len(search)-1
#             while left<=right:
#                 mid=(left+right)//2
#                 if search[mid]<number:
#                     left=mid+1
#                 else:
#                     right=mid-1
#             return left
#         perfect_sort=0
#         first=None
#         n=len(arr)
#         for i in range(n-1):
#             if arr[i]>arr[i+1]:
#                 if not first:
#                     first=i+1
#                 perfect_sort=i+1
#         search=arr[perfect_sort:]
#         count=float('inf')

#         # print(first,perfect_sort)
#         if first==0:
#             ind=binsearch(serach,arr[first])
#             ind=perfect_sort+ind
#             return (ind-first)-1
#         if first:
#             first-=1
#         while first!=None and first>=0:
#             ind=binsearch(search,arr[first])
#             ind=perfect_sort+ind
#             if first==0:
#                 count=min(count,(ind-first)-1,(perfect_sort-first))

#                 first-=1
#                 continue
#             count=min(count,(ind-first)-1)
#             # print(first,ind,count)
#             first-=1

#         return count if count!=float('inf') else 0
        
from typing import List
from bisect import bisect_left

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # Identify the prefix that is sorted
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If the entire array is sorted, no need to remove anything
        if left == n - 1:
            return 0

        # Identify the suffix that is sorted
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Minimum removals if we remove one of the unsorted middle parts entirely
        min_removals = min(n - left - 1, right)

        # Try to merge the prefix and suffix by removing elements in between
        for i in range(left + 1):
            # Find the smallest element in the suffix that is >= arr[i]
            pos = bisect_left(arr[right:], arr[i])
            # Compute the index in the original array
            if pos + right < n:
                min_removals = min(min_removals, (right - i - 1) + pos)

        return min_removals
