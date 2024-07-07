class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        bottles_drank = numBottles
        while numBottles >= numExchange:
            bottles_drank += (numBottles // numExchange)
            numBottles = (numBottles % numExchange) + (numBottles // numExchange)
        return bottles_drank
