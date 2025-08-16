class Solution {
    public int maximum69Number (int num) {
        StringBuilder nums = new StringBuilder(String.valueOf(num));

        int idx = nums.indexOf("6");  // find first '6'
        if (idx != -1) {
            nums.setCharAt(idx, '9'); // replace with '9'
        }

        return Integer.valueOf(nums.toString());
    }
}
