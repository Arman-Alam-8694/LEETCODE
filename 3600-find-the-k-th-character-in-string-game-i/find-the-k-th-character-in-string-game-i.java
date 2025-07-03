import java.util.*;
class Solution {
    public char kthCharacter(int k) {
        List<Character> list=new ArrayList<>();
        list.add('a');
        while(list.size()<k){
            int sz=list.size();
            for(int i=0;i<sz;i++){
                char c=list.get(i);
                char newChar = (char)(((c - 'a' + 1) % 26) + 'a');

                list.add(newChar);
            }

        }
        System.out.println(list);
        char answer=list.get(k-1);

        return answer;
    }
}