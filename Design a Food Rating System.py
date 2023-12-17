class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        index = self.foods.index(food)
        self.ratings[index] = newRating


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        item_num = 0
        dict_of_foods = {}
        for i in self.cuisines:
            if i == cuisine:
                dict_of_foods[self.foods[item_num]] = self.ratings[item_num]
            item_num += 1

        current_max_food = max(dict_of_foods, key=dict_of_foods.get)
        current_max_num = dict_of_foods[current_max_food]
        del dict_of_foods[current_max_food]
        if current_max_num in dict_of_foods.values():
            stack_of_highest = []
            stack_of_highest.append(current_max_food)
            for a, b in dict_of_foods.items():
                if b == current_max_num:
                    stack_of_highest.append(a)
            stack_of_highest.sort()
            return stack_of_highest[0]
        return current_max_food


foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9,12,8,15,14,7]
food = "sushi"
newRating = 16
food1 = "ramen"
newRating1 = 16
cuisine = "japanese"

# Your FoodRatings object will be instantiated and called as such:
obj = FoodRatings(foods, cuisines, ratings)
obj.changeRating(food,newRating)
obj.changeRating(food1,newRating1)
param_2 = obj.highestRated(cuisine)
print(param_2)