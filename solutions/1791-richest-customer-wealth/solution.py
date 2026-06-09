class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=0
        for account in accounts:
            ans=max(ans,sum(account))
        return ans

