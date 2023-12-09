import random
class apple:
    NumOfApples = TotalWeight = 0

    def __init__(self):
        self.weight = random.uniform(.2, .5)
        apple.TotalWeight += self.weight
        apple.NumOfApples += 1


for char in range(100):
    apple()

print("Number of apples: ", apple.NumOfApples)
print("Total weight: ", "{:.2f}".format(apple.TotalWeight))