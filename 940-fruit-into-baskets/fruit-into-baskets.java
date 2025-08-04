// class Solution:
//     def totalFruit(self, fruits: List[int]) -> int:
//         result=0
//         mapp=defaultdict(int)
//         left=0
//         n=len(fruits)
//         counts=0
//         for right in range(n):
//             mapp[fruits[right]]+=1
//             counts+=1
//             while len(mapp)>2:
//                 mapp[fruits[left]]-=1
//                 counts-=1
//                 if mapp[fruits[left]]==0:
//                     del mapp[fruits[left]]
//                 left+=1
//             result=max(result,counts)
//         return result
        

class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer,Integer> mapp=new HashMap<>();
        int count=0;
        int left=0;
        int answer=0;
        int n=fruits.length;
        for(int right=0;right<n;right++){
            mapp.put(fruits[right],mapp.getOrDefault(fruits[right],0)+1);
            count+=1;
            while(mapp.size()>2){
                int val=mapp.get(fruits[left]);
                val-=1;
                count-=1;
                if(val==0){
                    mapp.remove(fruits[left]);
                }else{
                    mapp.put(fruits[left],val);
                }
                left+=1;
            }
            answer=Math.max(answer,count);

        }
        return answer;
    }
}