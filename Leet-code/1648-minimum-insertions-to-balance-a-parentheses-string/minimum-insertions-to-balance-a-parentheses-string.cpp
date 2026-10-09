class Solution {
public:
    int minInsertions(string s) {
        int res = 0;   // Count of insertions needed
        int left = 0;  // Count of unmatched left parentheses '('
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                left++;
            } else { // s[i] == ')'
                // Check if the next character is also a ')'
                if (i + 1 < s.length() && s[i + 1] == ')') {
                    i++; // Skip the second ')'
                } else {
                    res++; // We need one more ')' to form '))'
                }
                
                if (left > 0) {
                    left--; // Match with an existing '('
                } else {
                    res++;  // We need a '(' to match this '))'
                }
            }
        }
        
        // Each remaining unmatched '(' needs two ')' characters
        return res + left * 2;
    }
};