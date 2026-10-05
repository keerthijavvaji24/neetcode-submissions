class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            key=sorted(i)
            key="".join(key)
            if key not in d:
                d[key]=[i]
            else:
                d[key].append(i)
        return list(d.values())
        

        