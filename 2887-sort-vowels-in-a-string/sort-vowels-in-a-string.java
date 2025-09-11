class Solution {
    public String sortVowels(String s) {
        List<Integer> indexx=new ArrayList<>();
        Set<Character> vowel=new HashSet<>(Arrays.asList('a','e','i','o','u','A','E','I','O','U'));

        List<Character> chhar=new ArrayList<>();
        for(int i=0;i<s.length();i++){
            if(vowel.contains(s.charAt(i))){
                indexx.add(i);
                chhar.add(s.charAt(i));

            }
        }
        Collections.sort(chhar);
        System.out.println(chhar);
        int pointer=0;
        StringBuilder answer=new StringBuilder();
        for(int i=0;i<s.length();i++){
            if((indexx.size()>pointer) && (indexx.get(pointer)==i)){
                answer.append(chhar.get(pointer));
                pointer+=1;
            }else{
                answer.append(s.charAt(i));
            }

        }
        return answer.toString();

       

        
    }
}