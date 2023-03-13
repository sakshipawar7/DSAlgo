# https://leetcode.com/problems/word-break-ii/

# DP + DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = {i : [] for i in range(len(s))}
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dic[i].append(word)
        
        res = []
        if not dic[0]: return res
        
        def solve(i, path):
            if i >= len(s):
                res.append(path)
                return
            for num in dic[i]:
                if path == "":
                    solve(i + len(num), num)
                else:
                    solve(i + len(num), path + " " + num)
        
        solve(0, "")
        return res

    
    
    
    
    
# DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[""]] * (n+1)
        for i in range(1, n+1):
            arr = []
            for word in wordDict:
                if i - len(word) >= 0 and s[i-len(word):i] == word:
                    if i-len(word) == 0:
                        arr.append(word)
                    elif dp[i-len(word)] != [""]:
                        for st in dp[i-len(word)]:
                            arr.append(st + " " + word)
                            
            dp[i] = arr
        # print(dp)
        return dp[-1]
