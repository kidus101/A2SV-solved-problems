class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_accounts = list()
        for account in accounts:
             sum_accounts.append(sum(account))
        return max(sum_accounts)