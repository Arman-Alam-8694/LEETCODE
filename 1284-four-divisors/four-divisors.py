class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        def check(x):
            if x==2:
                return 0
            temp=x+1
            till=math.ceil(math.sqrt(x))
            found=False
            store=set()
            print(x,till)
            for i in range(2,till+1):
                if x%i==0 and i not in store:
                    if found:
                        return 0
                    temp+=i
                    nxt=x//i
                    if nxt!=i:
                        temp+=nxt
                        found=True
                        store.add(nxt)
                        store.add(i)
                    else:
                        return 0
            # print(x,temp,found)
            return temp if found else 0
        for i in range(n):
            ans+=check(nums[i])
        return ans

        