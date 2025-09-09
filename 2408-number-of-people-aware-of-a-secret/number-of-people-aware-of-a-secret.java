class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        final int MOD = 1_000_000_007;
        long[] dp = new long[n + 1];      // dp[d] = number who learn on day d
        long[] events = new long[n + 2];  // events[d] = change in number of sharers starting on day d

        dp[1] = 1;
        // schedule day-1 learner's start/stop sharing events
        if (1 + delay <= n) events[1 + delay] = (events[1 + delay] + dp[1]) % MOD;
        if (1 + forget <= n) events[1 + forget] = (events[1 + forget] - dp[1] + MOD) % MOD;

        long sharers = 0;
        for (int day = 2; day <= n; day++) {
            // update current sharers from difference array
            sharers = (sharers + events[day]) % MOD;

            // number who learn today = current sharers
            dp[day] = sharers;

            if (dp[day] == 0) continue;
            int start = day + delay;
            int end = day + forget;
            if (start <= n) events[start] = (events[start] + dp[day]) % MOD;
            if (end <= n)   events[end]   = (events[end]   - dp[day] + MOD) % MOD;
        }

        long ans = 0;
        // those who still remember on day n are learners in [n-forget+1, n]
        for (int d = Math.max(1, n - forget + 1); d <= n; d++) {
            ans = (ans + dp[d]) % MOD;
        }
        return (int) ans;
    }
}
