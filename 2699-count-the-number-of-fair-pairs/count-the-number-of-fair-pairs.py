class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
       
        # smallest=float(inf)
        # for i in range(n):
        #     if not temp:
        #         smallest=nums[i]
        #         temp.append(smallest)
        #     else:
        #         low=binsearch(nums[i],temp)
        #         high=binsearch(nums[i],temp)
        def binsearch(target,lower,upper,tempn):
            ans=[]
            left=0
            right=len(tempn)-1
            while left<=right:
                mid=(left+right)//2
                if tempn[mid]+target>=lower:
                    right=mid-1
                else:
                    left=mid+1
            ans.append(left)
    
            left=0
            right=len(tempn)-1
            while left<=right:
                mid=(left+right)//2
                if tempn[mid]+target<=upper:
                    left=mid+1
                else:
                    right=mid-1
            ans.append(right)
            return ans


        n=len(nums)
      
        temp=sorted(nums)
        
        tempnext=[]
        n=len(nums)
        count=0
        for i in range(n):
            target=temp[i]
            if not tempnext:
                tempnext.append(target)
            else:
                low,high=binsearch(target,lower,upper,tempnext)
                # print(f"temp:{t/empnext},low={low},high={high}")
                if low==len(tempnext) or high==-1:
                    tempnext.append(target)
                elif low>high:
                    if high==-1:
                        count+=1
                        tempnext.append(target)
                    else:
                        tempnext.append(target)

                    
                elif low==high:
                    if lower<=tempnext[low]+target<=upper:
                        count+=1
                        tempnext.append(target)
                    else:
                        tempnext.append(target)
                else:
                    count+=(high-low)+1
                    tempnext.append(target)
                # print(count)



        return count