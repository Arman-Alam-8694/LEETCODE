import java.util.*;

class Solution {
    int[][] players;
    Integer[][] memo;

    public int bestTeamScore(int[] scores, int[] ages) {
        int n = scores.length;
        players = new int[n][2];
        
        // 1. Pair age and score
        for (int i = 0; i < n; i++) {
            players[i][0] = ages[i];
            players[i][1] = scores[i];
        }

        // 2. Sort by Age (primary) and Score (secondary)
        Arrays.sort(players, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

        // 3. Initialize memoization table
        // We use n + 1 for the second dimension to handle the -1 index case
        memo = new Integer[n][n + 1];

        return solve(0, -1, n);
    }

    private int solve(int idx, int prevIdx, int n) {
        if (idx == n) return 0;

        // prevIdx + 1 maps -1 to 0, 0 to 1, etc., for the memo table
        if (memo[idx][prevIdx + 1] != null) {
            return memo[idx][prevIdx + 1];
        }

        // Option 1: Skip the current player
        int res = solve(idx + 1, prevIdx, n);

        // Option 2: Pick the current player (if no conflict)
        if (prevIdx == -1 || players[idx][1] >= players[prevIdx][1]) {
            res = Math.max(res, players[idx][1] + solve(idx + 1, idx, n));
        }

        return memo[idx][prevIdx + 1] = res;
    }
}