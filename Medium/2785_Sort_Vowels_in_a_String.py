#1 pointer to string another to vowel list
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ("AEIOUaeiou")
        vow = []
        for letter in s:
            if letter in vowels:
                vow.append(letter)
        vow.sort()
        j = 0
        s = list(s)
        for i,letter in enumerate(s):
            if letter not in vowels:
                continue
            s[i] = vow[j]
            j+=1
        return "".join(s)
