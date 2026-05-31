class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        sum_ = 0
        mult = 1
        while n>0:
            r = n%10
            temp//=10
            sum_+=r
            mult *=r
            n//=10
        return    mult - sum_
        

        
