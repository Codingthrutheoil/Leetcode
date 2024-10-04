class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        point1, skill2 = len(skill)-1, (len(skill) // 2) - 1
        total = 0
        for a in range(skill2):
            if skill[a] + skill[point1] \
                    != skill[a + 1] + skill[point1-1]:
                return(-1)
            total += skill[a] * skill[point1]
            a += 1
            point1 -= 1

        total += skill[point1-1] * skill[point1]
        return(total)
