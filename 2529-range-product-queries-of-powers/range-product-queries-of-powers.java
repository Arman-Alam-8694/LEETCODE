import java.util.*;

class Solution {
    public int[] productQueries(int n, int[][] queries) {
        long mod = 1_000_000_007L;

        // Step 1: Get powers of 2 from binary representation
        String binary = Integer.toBinaryString(n);
        List<Integer> powers = new ArrayList<>();
        int cur = 0;
        for (int i = binary.length() - 1; i >= 0; i--) {
            if (binary.charAt(i) == '1') {
                powers.add(1 << cur);
            }
            cur++;
        }

        // Step 2: Process each query directly
        int[] answer = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];
            long product = 1;
            for (int i = l; i <= r; i++) {
                product = (product * powers.get(i)) % mod;
            }
            answer[q] = (int) product;
        }

        return answer;
    }
}
