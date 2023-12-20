class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        in_money = money
        num = 0
        prices.sort()
        num_of_choc = []
        for i in prices:
            if money - i < 0:
                continue
            else:
                money -= prices[num]
                num_of_choc.append(1)
            num += 1
            if len(num_of_choc) == 2:
                break
        return money if len(num_of_choc) == 2 else in_money