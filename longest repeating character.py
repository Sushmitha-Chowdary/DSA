class Solution:
    def characterReplacement(self,s,k):
        n=len(s)
        ans =0
        for i in range(n):
            freq=[0]*26
            mf=0
            for j in range(i,n):
                idx=ord(s[j])-ord('A')
                freq[idx]+=1
                mf=max(mf,freq[idx])
                if (j-i+1)-mf<= k:
                    ans = max(ans,j-i+1)
        return ans
s="ABAB"
k=2
sol = Solution()
print(sol.characterReplacement(s,k))
    #time limit exceeded