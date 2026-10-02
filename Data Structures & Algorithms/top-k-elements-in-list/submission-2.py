class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            if i  in f:
                f[i]+=1
            else:
                f[i]=1
        result = sorted(f, key=f.get, reverse=True)
        result=result[:k]
        return result

