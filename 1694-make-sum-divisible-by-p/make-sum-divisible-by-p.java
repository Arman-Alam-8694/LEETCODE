class Solution {
    public int minSubarray(int[] nums, int p) {
        int n = nums.length;
        int[] parray = new int[n + 1];

        // Prefix sum modulo p
        for (int i = 0; i < n; i++) {
            parray[i + 1] = (parray[i] + nums[i]) % p;
        }

        int total = parray[n];
        if (total % p == 0) return 0;

        HashMap<Integer, Integer> map = new HashMap<>();
        int maxx = 0;

        for (int i = 0; i < n; i++) {
            int second = ((total - parray[i]) % p + p) % p;
            int first = ((total - second) % p + p) % p;

            int slen = n - i;
            int flen = n - slen;

            int temp = (p - second) % p;

            if (first == 0) {
                maxx = Math.max(maxx, flen);
            }

            if (second == 0 && map.containsKey(0)) {
                maxx = Math.max(maxx, map.get(0) + slen);
            }

            if (map.containsKey(temp)) {
                maxx = Math.max(maxx, map.get(temp) + slen);
            }

            if (map.containsKey(first)) {
                map.put(first, Math.max(map.get(first), flen));
            } else {
                map.put(first, flen);
            }
        }

        return maxx != 0 ? n - maxx : -1;
    }
}
