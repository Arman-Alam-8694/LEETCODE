import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private List<Integer> powers; 
    private List<List<Integer>> memo; // memo[idx][remaining]

    public int numberOfWays(int n, int x) {
        // Step 1: Generate all powers i^x <= n
        powers = new ArrayList<>();
        int i = 1;
        while (Math.pow(i, x) <= n) {
            powers.add((int) Math.pow(i, x));
            i++;
        }

        // Step 2: Initialize memoization table as a list of lists
        memo = new ArrayList<>();
        for (int idx = 0; idx < powers.size(); idx++) {
            List<Integer> row = new ArrayList<>(Collections.nCopies(n + 1, null));
            memo.add(row);
        }

        // Step 3: Start recursion
        return dfs(0, n);
    }

    private int dfs(int idx, int remaining) {
        // Base case: exactly reached sum
        if (remaining == 0) {
            return 1;
        }
        // Base case: no more numbers or sum went negative
        if (idx >= powers.size() || remaining < 0) {
            return 0;
        }
        // Check memo
        if (memo.get(idx).get(remaining) != null) {
            return memo.get(idx).get(remaining);
        }

        // Option 1: Skip current number
        long ways = dfs(idx + 1, remaining);

        // Option 2: Take current number
        ways += dfs(idx + 1, remaining - powers.get(idx));

        // Store and return modulo MOD
        int result = (int) (ways % MOD);
        memo.get(idx).set(remaining, result);
        return result;
    }
}
