class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxi = 0

        for i in range(n):
            myset = set()

            for j in range(i, n):
                if s[j] in myset:
                    break

                myset.add(s[j])
                maxi = max(maxi, j - i + 1)

        return maxi

# another method
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict1 = {}
        n = len(s)
        l = 0
        r = 0 
        maxi = 0
        while r<n:
            if s[r]in dict1:
                l = max(l,dict1[s[r]]+1)

            
            maxi = max(maxi,r-l+1)
            dict1 [s[r]] = r
            r +=1
        return maxi

