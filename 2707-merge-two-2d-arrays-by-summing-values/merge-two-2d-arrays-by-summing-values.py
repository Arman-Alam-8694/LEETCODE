class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # ptr=0
        # i=0
        # n=len(nums2)
        # result=[]
        # n1=len(nums1)
        # while i<n or ptr<n1:
        #     if ptr==n1:
        #         result.append([nums2[i][0],nums2[i][1]])
        #         i+=1
        #     elif i==n:
        #         result.append([nums1[ptr][0],nums1[ptr][1]])
        #         ptr+=1

        #     elif nums1[ptr][0]==nums2[i][0]:
        #         result.append([nums2[i][0],nums2[i][1]+nums1[ptr][1]])
        #         ptr+=1
        #         i+=1
        #     elif nums2[i][0]<nums1[ptr][0]:
        #         result.append([nums2[i][0],nums2[i][1]])
        #         i+=1
        #     else:
        #         result.append([nums1[ptr][0],nums1[ptr][1]])
        #         ptr+=1

        # return result

        left=0
        n=len(nums1)
        right=0
        n2=len(nums2)
        result=[]

        while left<n and right<n2:
            if nums1[left][0]==nums2[right][0]:
                result.append([nums1[left][0],nums1[left][1]+nums2[right][1]])
                left+=1
                right+=1
            elif nums1[left][0]<nums2[right][0]:
                result.append([nums1[left][0],nums1[left][1]])
                left+=1
            else:
                result.append([nums2[right][0],nums2[right][1]])
                right+=1

        while left<n:
            result.append([nums1[left][0],nums1[left][1]])
            left+=1
        while right<n2:
              result.append([nums2[right][0],nums2[right][1]])
              right+=1
        return result




        