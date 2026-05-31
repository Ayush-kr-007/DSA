class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c = 0
        num1 = num
        while num1 >0:
            r = num1%10
            if num%r==0:
                c+=1
            num1//=10
        return c

