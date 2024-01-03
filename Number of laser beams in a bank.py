class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        counter_first = bank[0].count("1")
        final_counter = counter_last = 0
        for a in bank[1:]:
            counter_last = a.count("1")
            final_counter += (counter_first * counter_last)
            if counter_last != 0:
                counter_first = counter_last
        return final_counter