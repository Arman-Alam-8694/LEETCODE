class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;
        int[] answer = new int[row * col];
        int count = 0;
        int total = row * col;

        // start position
        int sr = 0; 
        int sc = 0;

        while (count < total) {
            // Move upward-right
            while (true) {
                answer[count++] = mat[sr][sc];
                int nextr = sr - 1;
                int nextc = sc + 1;
                sr = nextr;
                sc = nextc;

                if (sc >= col) {
                    sr = nextr + 2;
                    sc = nextc - 1;
                    break;
                } else if (nextr < 0) {
                    sr = nextr + 1;
                    sc = nextc;
                    break;
                }
            }

            if (count >= total) break;

            // Move downward-left
            while (true) {
                answer[count++] = mat[sr][sc];
                int nextr = sr + 1;
                int nextc = sc - 1;
                sr = nextr;
                sc = nextc;

                if (nextr >= row) {
                    sr = nextr - 1;
                    sc = nextc + 2;
                    break;
                } else if (nextc < 0) {
                    sr = nextr;
                    sc = nextc + 1;
                    break;
                }
            }
        }

        return answer;
    }
}
// class Solution:
//     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
//         row=len(mat)
//         col=len(mat[0])
//         start=[0,0]
//         answer=[]
//         count=0
//         total=row*col
//         while count<total:
//             while True:
//                 curr=start[0]
//                 curc=start[1]
//                 answer.append(mat[curr][curc])
//                 count+=1
//                 nextr=curr-1
//                 nextc=curc+1
//                 start=[nextr,nextc]
//                 if nextc>=col:
//                     start=[nextr+2,nextc-1]
//                     break
//                 elif nextr<0:
//                     start=[nextr+1,nextc]
//                     break
            
//             if count>=total:
//                 break
//             while True:
//                 curr=start[0]
//                 curc=start[1]
//                 answer.append(mat[curr][curc])
//                 count+=1
//                 nextr=curr+1
//                 nextc=curc-1
//                 start=[nextr,nextc]
//                 if nextr>=row:
//                     start=[nextr-1,nextc+2]
//                     break
//                 elif nextc<0:
//                     start=[nextr,nextc+1]
//                     break

//         return answer

                


        