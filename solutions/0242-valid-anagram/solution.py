class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a ={}
        b=  {}
        for i in s:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for j in t:
            if j not in b:
                b[j]=1
            else:
                b[j]+=1
        if a ==b:
            return True
        else:
            return False
