class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        st = [0]*len(s)
        k = 0
        for i in indices:
            st[i] = s[k]
            k += 1
        ans = "".join(st)
        return ans