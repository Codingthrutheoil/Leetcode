class Solution(object):
    def totalMoney(self, n):
        iterations_of_ten = n // 7
        balance_days = n % 7 if n != 7 else 0
        final_result = 0
        monday_value = 1
        if iterations_of_ten > 0:
            for i in range(iterations_of_ten):
                for a in range(1, 8):
                    final_result += i + a
                monday_value += 1
            if balance_days != 0:
                for i in range(1, balance_days + 1):
                    final_result += monday_value
                    monday_value += 1

        else:
            for i in range(1, balance_days + 1):
                final_result += i
        return final_result