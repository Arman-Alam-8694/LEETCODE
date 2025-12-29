import java.util.*;

class Solution {

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        // Build transition map
        Map<String, List<Character>> map = new HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0, 2);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s.charAt(2));
        }

        return backtrack(bottom.length(), 0, 1, bottom, new StringBuilder(), map);
    }

    private boolean backtrack(
            int stage,
            int i,
            int j,
            String bottom,
            StringBuilder nxt,
            Map<String, List<Character>> map) {

        // Base case
        if (stage == 1) {
            return true;
        }

        // ✅ Fail-fast pruning on full row
        if (i == 0 && j == 1) {
            for (int x = 0; x < bottom.length() - 1; x++) {
                if (!map.containsKey(bottom.substring(x, x + 2))) {
                    return false;
                }
            }
        }

        String pair = "" + bottom.charAt(i) + bottom.charAt(j);

        if (map.containsKey(pair)) {
            for (char ch : map.get(pair)) {
                nxt.append(ch);

                // Finished building next row
                if (j == stage - 1) {
                    if (backtrack(stage - 1, 0, 1,
                                  nxt.toString(), new StringBuilder(), map)) {
                        return true;
                    }
                } else {
                    if (backtrack(stage, i + 1, j + 1,
                                  bottom, nxt, map)) {
                        return true;
                    }
                }

                nxt.deleteCharAt(nxt.length() - 1);
            }
        }

        return false;
    }
}
