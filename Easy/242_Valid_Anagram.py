#11ms dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphas = {}

        for i in range(len(s)):
            alphas[s[i]] = alphas.get(s[i],0) + 1
            alphas[t[i]] = alphas.get(t[i],0) - 1

        for c in alphas.values():
            if c != 0: 
                return False

        return True

#15ms arrays
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphas = {}

        for i in range(len(s)):
            alphas[s[i]] = alphas.get(s[i],0) + 1
            alphas[t[i]] = alphas.get(t[i],0) - 1

        for c in alphas.values():
            if c != 0: 
                return False

        return True
# counter function can also be used to implement this
''' from collections import Counter
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            return Counter(s) == Counter(t)'''
