class Solution {
    public int countPalindromicSubsequence(String s) {

        // Get distinct characters in the string
        Set<Character> chars = new HashSet<>();
        for (char c : s.toCharArray()) {
            chars.add(c);
        }

        int answer = 0;

        // For each distinct character
        for (char c : chars) {
            Set<Character> done = new HashSet<>();
            Set<Character> temp = new HashSet<>();
            boolean found = false;

            for (int j = 0; j < s.length(); j++) {
                char ch = s.charAt(j);

                // If same char found again after first occurrence
                if (ch == c && found) {
                    if (!temp.isEmpty()) {
                        done.addAll(temp);
                        temp.clear();
                        temp.add(c);
                    } else {
                        temp.add(c);
                    }
                }
                // First time encountering c
                else if (ch == c) {
                    found = true;
                }
                // Characters between the two occurrences of c
                else if (found) {
                    if (!done.contains(ch)) {
                        temp.add(ch);
                    }
                }
            }

            answer += done.size();
        }

        return answer;
    }
}
