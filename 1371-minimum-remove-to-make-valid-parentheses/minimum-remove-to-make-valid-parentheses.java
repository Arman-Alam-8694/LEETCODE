import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Integer> stack = new Stack<>();
        Set<Integer> removeSet = new HashSet<>();

        // Step 1: find all invalid indices
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                stack.push(i); // store index of '('
            } 
            else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop(); // valid pair found
                } else {
                    removeSet.add(i); // extra ')'
                }
            }
        }

        // Step 2: add any remaining '(' indices to removeSet
        while (!stack.isEmpty()) {
            removeSet.add(stack.pop());
        }

        // Step 3: build result skipping invalid indices
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!removeSet.contains(i)) {
                result.append(s.charAt(i));
            }
        }

        return result.toString();
    }
}
