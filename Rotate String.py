class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s_list = list(s)
        goal_list = list(goal)

        for a in range(len(goal)):
            if s_list == goal_list:
                return True
            s_list = s_list[1:] + list(s_list[0])
        return False
