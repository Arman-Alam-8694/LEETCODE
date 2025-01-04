class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Store unique palindromes
        unique_palindromes = set()
        n = len(s)
        
        # Iterate for each character 'a' to 'z' as the outer characters of the palindrome
        for char in "abcdefghijklmnopqrstuvwxyz":
            # Find the first and last occurrence of the character in the string
            first = s.find(char)
            last = s.rfind(char)
            
            # Only consider cases where the character appears at least twice
            if first != -1 and last != -1 and first < last:
                # Extract the substring between the first and last occurrence
                middle_chars = set(s[first + 1:last])
                # Form all palindromes of the form char + middle_char + char
                for mid_char in middle_chars:
                    unique_palindromes.add(char + mid_char + char)
        
        # Return the count of unique palindromes
        return len(unique_palindromes)
