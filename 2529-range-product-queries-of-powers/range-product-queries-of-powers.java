import java.util.*;
import java.math.BigInteger;

class Solution {
    public int[] productQueries(int n, int[][] queries) {
        long mod = 1_000_000_007L;

        String binary = Integer.toBinaryString(n);
        List<Integer> powers = new ArrayList<>();
        int cur = 0;
        for (int i = binary.length() - 1; i >= 0; i--) {
            if (binary.charAt(i) == '1') {
                powers.add(1 << cur);
            }
            cur++;
        }

        // Prefix with BigInteger
        BigInteger[] prefix = new BigInteger[powers.size()];
        prefix[0] = BigInteger.valueOf(powers.get(0));
        for (int i = 1; i < powers.size(); i++) {
            prefix[i] = prefix[i - 1].multiply(BigInteger.valueOf(powers.get(i)));
        }

        int[] answer = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];
            BigInteger product;
            if (l == 0) {
                product = prefix[r];
            } else {
                product = prefix[r].divide(prefix[l - 1]);
            }
            answer[q] = product.mod(BigInteger.valueOf(mod)).intValue();
        }

        return answer;
    }
}
