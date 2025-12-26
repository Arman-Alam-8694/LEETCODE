class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {

        int total = 0;
        for (int a : apple) total += a;

        // Find max capacity
        int maxCap = 0;
        for (int c : capacity) {
            if (c > maxCap) maxCap = c;
        }

        // Count frequencies
        int[] freq = new int[maxCap + 1];
        for (int c : capacity) {
            freq[c]++;
        }

        int used = 0;
        int sum = 0;

        // Traverse from largest capacity
        for (int cap = maxCap; cap >= 0; cap--) {
            while (freq[cap]-- > 0) {
                sum += cap;
                used++;
                if (sum >= total) {
                    return used;
                }
            }
        }
        return used;
    }
}
