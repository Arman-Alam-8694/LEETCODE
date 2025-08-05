class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = fruits.length;
        int unplaced = 0;

        for (int i = 0; i < n; i++) {
            boolean placed = false;

            // Always look from the start to find leftmost available basket
            for (int j = 0; j < n; j++) {
                if (baskets[j] != -1 && baskets[j] >= fruits[i]) {
                    baskets[j] = -1;  // Mark as used
                    placed = true;
                    break;
                }
            }

            if (!placed) {
                unplaced++;
            }
        }

        return unplaced;
    }
}
