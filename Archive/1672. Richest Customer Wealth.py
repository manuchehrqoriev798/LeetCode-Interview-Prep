class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth





class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maximum = 0

        for costumers in range(len(accounts)):
            temp = 0
            for each_costumer in range(len(accounts[costumers])):
                temp += accounts[costumers][each_costumer]
            maximum = max(temp, maximum)
        return maximum







class Solution:
    def maximumWealth(self, accounts) -> int:
        return max(map(sum, accounts))