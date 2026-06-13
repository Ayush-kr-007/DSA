class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for index in range(len(s)):
                    if freq[s[index]] == 1:
                        return index
                        
        return -1
        
