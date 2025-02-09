class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #NDBM

        # HERE THE KEY POINT IS OBSERVATON IN THE EQUATION OR FORMING A RELATION BETWEEN THE 
        #INDICES AND ELEMENTS SUCH THAT IT BECOMES EASIER TO LOOK BACK BECAUSE WE WON'T BE 
        #KNOWING THE FUTURE OF WHAT WILL BE COMING NEXT SO WE WILL TWIST THE QUESITON IN 
        #FINDING THE TOTAL NO. OF GOOD PAIRS AND THEN JUST SUBTRACTING IT WITH THE TOTAL NO. OF 
        #PAIRS  the equation could be nums[i]-i==nums[j]-j for good pairs

        count=defaultdict(int)
        n=len(nums)-1
        totalPairs=(n*(n+1))//2
        goodPairs=0
        n+=1
        for i in range(n):
            slope=nums[i]-i
            goodPairs+=count[slope]
            count[slope]+=1
        return totalPairs-goodPairs


        
