import java.util.*;

class Solution {
    public int numberOfPairs(int[][] points) {
        // Sort by x descending, then y ascending
        Arrays.sort(points, (a, b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(b[0], a[0]);
        });

        int ans = 0;
        int n = points.length;

        for (int j = 0; j < n; ++j) {       // left → right over mirrored order
            int y = points[j][1];
            int mny = Integer.MAX_VALUE;    // track min yy so far
            for (int i = j + 1; i < n; ++i) {
                int yy = points[i][1];
                // Mirror of: if (yy >= mny || yy < y) continue;
                if (yy < y || yy >= mny) continue;
                ans++;
                mny = yy;
            }
        }
        return ans;
    }
}
