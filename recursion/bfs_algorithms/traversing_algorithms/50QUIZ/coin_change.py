class Solution:

    def coinChangeRec(self, coins, amount):

        if amount == 0:
            return 0

        minCoins = float("inf")

        for coin in coins:
            if(amount - coin) >= 0:
                minCoins = min(minCoins, 1 + self.coinChange(coins, amount-coin))
        return minCoins
    
    def coinChange(self, coins, amount):
        minCoins = self.coinChangeRec(coins, amount)

        return -1 if minCoins == float("inf") else minCoins

    def coinChange2(self, coins, amount):
        nbCoinsArr = [float("inf")] * (amount + 1)
        nbCoinsArr[0] = 0
        for i in range(1, amount + 1):
            minCoins = float("inf")

            for coin in coins:
                if(i - coin) >= 0:
                    minCoins = min(minCoins, 1 + nbCoinsArr[i - coin])
            nbCoinsArr[i] = minCoins
        
        return -1 if nbCoinsArr[amount] == float("inf") else nbCoinsArr[amount]
            

sln = Solution()

coins = [1,2,5]
amount = 11

print(sln.coinChange(coins, amount))
print(sln.coinChange2(coins, amount))