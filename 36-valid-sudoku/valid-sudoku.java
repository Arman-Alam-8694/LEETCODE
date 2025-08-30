class Solution {
    public boolean isValidSudoku(char[][] board) {
        int row=board.length;
        int col=board[0].length;
        List<HashSet<Character>> rows= new ArrayList<>();
        List<HashSet<Character>> cols= new ArrayList<>();
        for(int i=0;i<row;i++){
            rows.add(new HashSet<Character>());
        }
        for(int i=0;i<col;i++){
            cols.add(new HashSet<Character>());
        }

        
        for(int r=0;r<row;r+=3){
            
            for(int c=0;c<col;c+=3){
                HashSet<Character> curr=new HashSet<>();
                for(int tr=r;tr<r+3;tr++){
                    for(int tc=c;tc<c+3;tc++){
                        char value=board[tr][tc];
                       
                        if(value!='.'){
                            if(rows.get(tr).contains(value) | cols.get(tc).contains(value)|curr.contains(value)){
                         
                                return false;
                            }
                            rows.get(tr).add(value);
                            cols.get(tc).add(value);
                            curr.add(value);
                        }

                    }
                }

            }
        }
        return true;
    }
}