class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_res = [0] * 27
        t_res = [0] * 27
        for i in range(len(s)):
            s_index = (ord(s[i]) - ord('a'))
            s_res[s_index] += 1
            t_index = (ord(t[i]) - ord('a'))
            t_res[t_index] += 1

        for i in range(len(s_res)):
            if s_res[i] != t_res[i]:
                return False

        return True