class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0
        if len(s) == 2:
            return 2 if s == "()" else 0
        
        # dp[i] => longest valid substring ending at index i
        dp = [0]*len(s)
        
        if s[0] == "(" and s[1] == ")":
            dp[1] = 2
            
        highest = dp[1]
        
        for i in range(2, len(s)):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            if s[i] == ")" and s[i-1] == ")":
                if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
            highest = max(highest, dp[i])
        return highest
