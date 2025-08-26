import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<List<Object>> stack = new Stack<>();
        List<Integer> extra = new ArrayList<>();

        // Step 1: Traverse the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                // push (char, index) as list
                stack.push(Arrays.asList(c, i));
            } 
            else if (c == ')') {
                if (!stack.isEmpty() && (char) stack.peek().get(0) == '(') {
                    stack.pop(); // valid pair, remove
                } else {
                    extra.add(i); // unmatched ')'
                }
            }
        }

        // Step 2: add any leftover '(' indices from the stack
        while (!stack.isEmpty()) {
            extra.add((int) stack.pop().get(1)); // get index of '('
        }

        // Step 3: build final string, skipping invalid indices
        StringBuilder result = new StringBuilder();
        Set<Integer> removeSet = new HashSet<>(extra);
        for (int i = 0; i < s.length(); i++) {
            if (!removeSet.contains(i)) {
                result.append(s.charAt(i));
            }
        }

        return result.toString();
    }
}
