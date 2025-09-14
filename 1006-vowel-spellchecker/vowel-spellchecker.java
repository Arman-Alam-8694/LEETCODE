import java.util.*;

class Solution {
    private String devowel(String word) {
        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            if ("aeiou".indexOf(Character.toLowerCase(c)) >= 0) {
                sb.append('*');
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }
        return sb.toString();
    }

    public String[] spellchecker(String[] wordlist, String[] queries) {
        // 1. Exact match set
        Set<String> exactWords = new HashSet<>(Arrays.asList(wordlist));

        // 2. Case-insensitive map
        Map<String, String> caseInsensitiveMap = new HashMap<>();

        // 3. Vowel-error map
        Map<String, String> vowelMap = new HashMap<>();

        for (String word : wordlist) {
            String lower = word.toLowerCase();
            caseInsensitiveMap.putIfAbsent(lower, word);

            String devowelWord = devowel(word);
            vowelMap.putIfAbsent(devowelWord, word);
        }

        // Process queries
        String[] result = new String[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String q = queries[i];

            if (exactWords.contains(q)) {
                result[i] = q;  // Rule 1: exact match
            } else {
                String lowerQ = q.toLowerCase();
                if (caseInsensitiveMap.containsKey(lowerQ)) {
                    result[i] = caseInsensitiveMap.get(lowerQ);  // Rule 2
                } else {
                    String devowelQ = devowel(q);
                    if (vowelMap.containsKey(devowelQ)) {
                        result[i] = vowelMap.get(devowelQ);  // Rule 3
                    } else {
                        result[i] = "";  // No match
                    }
                }
            }
        }
        return result;
    }
}
