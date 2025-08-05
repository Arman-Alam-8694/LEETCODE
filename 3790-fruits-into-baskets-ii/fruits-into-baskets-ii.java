class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.length;
        int unplaced = 0;
        int leftMost=0;
        int j=leftMost;

        for (int i = 0; i < n; i++) {
            boolean placed = false;

            // Always look from the start to find leftmost available basket
            for (j = leftMost; j < n; j++) {
                if (baskets[j] != -1 && baskets[j] >= fruits[i]) {
                    baskets[j] = -1;  // Mark as used
                    placed = true;
                    break;
                }
            }
            if(j==(leftMost)){
                leftMost+=1;

            }

            if (!placed) {
                unplaced++;
            }
        }

        return unplaced;
    }
}
