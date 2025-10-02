class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int answer=0;
        int empty=0;
        int newB=numBottles;
        while(numBottles>=numExchange){
            answer+=newB;
            newB=0;
            while(numExchange<=numBottles){
                newB+=1;
                numBottles-=numExchange;
                numExchange+=1;


            }
            empty=numBottles;
            numBottles=newB+empty;

        }
        answer+=newB;
        return answer;
        
    }
}