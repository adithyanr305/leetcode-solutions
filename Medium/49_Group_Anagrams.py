class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(words)    
        return list(hmap.values())
