class FindSumPairs:


    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.map1=Counter(nums1)
        self.map2=Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        self.map2[self.nums2[index]]-=1
        if self.map2[self.nums2[index]]==0:
            del self.map2[self.nums2[index]]

        self.nums2[index]+=val
        if self.nums2[index] in self.map2:
            self.map2[self.nums2[index]]+=1
        else:
            self.map2[self.nums2[index]]=1
        

    def count(self, tot: int) -> int:
        self.answer=0
        for i,j in self.map1.items():
            if i<=tot:
                target=tot-i
                if target in self.map2:
                   
                    self.answer+=j*self.map2[target]
        return self.answer

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)