class Solution {
    public int maximum69Number (int num) {
        String s = String.valueOf(num);   // convert int → String
        int idx = s.indexOf('6');         // find first '6'

        if (idx != -1) {
            // replace only the first '6'
            s = s.substring(0, idx) + '9' + s.substring(idx + 1);
        }

        return Integer.parseInt(s);       // convert back to int
    }
}
