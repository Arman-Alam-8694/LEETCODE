class Solution {
    private static final int MOD = 1_000_000_007;
    private int[] powers;
    private Integer[][] memo; // memo[idx][remaining]

    public int numberOfWays(int n, int x) {
        // Step 1: Generate all powers i^x <= n
        int count = 0;
        int i = 1;
        while (Math.pow(i, x) <= n) {
            count++;
            i++;
        }
        powers = new int[count];
        for (int j = 0; j < count; j++) {
            powers[j] = (int) Math.pow(j + 1, x);
        }

        // Step 2: Initialize memoization table
        memo = new Integer[powers.length][n + 1];

        // Step 3: Start recursion from idx = 0, remaining sum = n
        return dfs(0, n);
    }

    private int dfs(int idx, int remaining) {
        // Base case: exactly reached sum
        if (remaining == 0) {
            return 1;
        }
        // Base case: no more numbers or sum went negative
        if (idx >= powers.length || remaining < 0) {
            return 0;
        }
        // Check memo
        if (memo[idx][remaining] != null) {
            return memo[idx][remaining];
        }

        // Option 1: Skip current number
        long ways = dfs(idx + 1, remaining);

        // Option 2: Take current number
        ways += dfs(idx + 1, remaining - powers[idx]);

        // Store and return modulo MOD
        memo[idx][remaining] = (int) (ways % MOD);
        return memo[idx][remaining];
    }
}
