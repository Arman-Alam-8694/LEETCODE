class Solution {

    private long get(int num) {
        if (num <= 0) return 0;
        long cnt = 0;
        int i = 0;
        long base = 1;
        while (base <= num) {
            long end = Math.min(base * 4 - 1, (long) num);
            long count = end - base + 1;
            cnt += (long) (i + 1) * count;  // each number in this block takes (i+1) steps
            i++;
            base *= 4;
        }
        return cnt;
    }

    public long minOperations(int[][] queries) {
        long res = 0;
        for (int[] q : queries) {
            long count1 = get(q[1]);
            long count2 = get(q[0] - 1);
            long totalSteps = count1 - count2;
            res += (totalSteps + 1) / 2; // ceil division
        }
        return res;
    }
}
