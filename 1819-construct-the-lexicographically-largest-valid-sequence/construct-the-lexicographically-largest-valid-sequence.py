class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        listt=[-1]*((n-1)*2+1)
        numbers=[i for i in range(n,0,-1)]
        print(numbers)
     

        def largest_form(numbers,curr_pos,listt):
            print(listt)
            if not numbers:
                print(listt)
                return True
            backtrack=False
            while listt[curr_pos]!=-1:
                curr_pos+=1
            for i in numbers:
                if i==1:
                    right_pos=curr_pos
                else:
                    right_pos=curr_pos+i
                if right_pos<len(listt) and listt[right_pos]==-1:
                    listt[right_pos]=i
                    listt[curr_pos]=i
                    numbers.remove(i)
                   
                    if not largest_form(numbers,curr_pos+1,listt):
                        listt[right_pos]=-1
                        listt[curr_pos]=-1
                        numbers.append(i)
                        numbers.sort(reverse=True)
                        backtrack=True

                        
                    else:
                        return True



            if not backtrack and listt[curr_pos]==-1:
                return False

        largest_form(numbers,0,listt)
        return listt
                



        