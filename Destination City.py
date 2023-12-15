class Solution:
    def destCity(self, paths):
        cities = set()
        dest = ""

        for path in paths:
            cities.add(path[0])

        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest

        return ""
