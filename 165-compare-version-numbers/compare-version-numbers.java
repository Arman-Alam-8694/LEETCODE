import java.util.*;

class Solution {
    public int compareVersion(String version1, String version2) {
        int[] v1 = Arrays.stream(version1.split("\\."))
                         .mapToInt(Integer::parseInt)
                         .toArray();

        int[] v2 = Arrays.stream(version2.split("\\."))
                         .mapToInt(Integer::parseInt)
                         .toArray();

        int size = Math.max(v1.length, v2.length);

        for (int i = 0; i < size; i++) {
            int first = (i < v1.length) ? v1[i] : 0;
            int second = (i < v2.length) ? v2[i] : 0;

            if (first > second) return 1;
            if (first < second) return -1;
        }

        return 0;
    }
}
