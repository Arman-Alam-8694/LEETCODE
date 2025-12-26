class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {

        int total = IntStream.of(apple).sum();

        // Sort primitive array (much faster)
        Arrays.sort(capacity); // ascending

        int temp = 0;
        int count = 0;

        // Traverse from largest to smallest
        for (int i = capacity.length - 1; i >= 0; i--) {
            temp += capacity[i];
            count++;
            if (temp >= total) {
                return count;
            }
        }
        return count;
    }
}
