import java.util.*;

class Solution {
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        Set<Integer> bannedSet = new HashSet<>();
        for (int b : banned) bannedSet.add(b);

        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        ans[p] = 0; // starting position takes 0 moves

        // Split unvisited indices by parity, ignoring banned and starting position
        TreeSet<Integer> evenSet = new TreeSet<>();
        TreeSet<Integer> oddSet  = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            if (i != p && !bannedSet.contains(i)) {
                if (i % 2 == 0) evenSet.add(i);
                else oddSet.add(i);
            }
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(p);

        while (!q.isEmpty()) {
            int pos = q.poll();
            int d = ans[pos];

            // Compute start interval for reversals containing pos
            int start_min = Math.max(0, pos - (k - 1));
            int start_max = Math.min(pos, n - k);
            if (start_min > start_max) continue;

            // Compute the interval of new positions reachable in 1 move
            int new_low = 2 * start_min + (k - 1) - pos;
            int new_high = 2 * start_max + (k - 1) - pos;
            if (new_low > new_high) {
                int tmp = new_low;
                new_low = new_high;
                new_high = tmp;
            }

            // Clip to array bounds
            int L = Math.max(0, new_low);
            int R = Math.min(n - 1, new_high);

            // Determine parity of reachable positions for this move
            int parity_needed = (k - 1 - pos) & 1; // 0 = even, 1 = odd
            TreeSet<Integer> paritySet = (parity_needed == 0) ? evenSet : oddSet;

            // Get all elements in [L,R] directly using subSet
            for (Integer x : new ArrayList<>(paritySet.subSet(L, true, R, true))) {
                ans[x] = d + 1;
                q.add(x);
                paritySet.remove(x);
            }
        }

        return ans;
    }
}
