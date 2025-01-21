class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        #time O(2*n*m) and space O(n*m+(n+m))

        row_count = len(mat)
        col_count = len(mat[0])

        row_remaining = [col_count] * row_count
        col_remaining = [row_count] * col_count

        value_to_position = {}
        for i in range(row_count):
            for j in range(col_count):
                value_to_position[mat[i][j]] = (i, j)

        for index, value in enumerate(arr):
            x, y = value_to_position[value]
            row_remaining[x] -= 1
            col_remaining[y] -= 1
            if row_remaining[x] == 0 or col_remaining[y] == 0:
                return index

        # in this question you should have just focused on what the question is asking 
        #like the smallest index so we think about how we can get that index 
        #we could reach to this observation of finding the smallest index out of  max_index of group of all elements in each row and column 
        #this means if we have such a index  which is smallest and if we reach till that index 
        #all the elements of that particular row and coloumn will be filled  
        #because that'a also the largets index of that particular row and coloumn

        #time O(3*N*M) ,SPACE ONLY O(N*M) ELIMINATED (n+m) slower though
        # mapp=defaultdict(int)
        # row=len(mat)
        # col=len(mat[0])
        # for i in range(row*col):
        #     mapp[arr[i]]=i
        # result=float('inf')
        # for i in range(row):
        #     temp=float('-inf')
        #     for j in range(col):
        #         temp=max(temp,mapp[mat[i][j]])
        #     result=min(temp,result)
        # for i in range(col):
        #     temp=float('-inf')
        #     for j in range(row):
        #         temp=max(temp,mapp[mat[j][i]])
        #     result=min(temp,result)
        # return result
        
                





    