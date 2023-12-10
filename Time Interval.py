class timeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        for argutypes in [hours, minutes, seconds]:
            if type(argutypes) != int:
                raise TypeError
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        while self.seconds > 59:
            self.minutes += self.seconds // 60
            self.seconds %= 60

        while self.minutes > 59:
            self.hours += self.minutes // 60
            self.minutes %= 60

        return (str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        return self

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds
        return self

    def __mul__(self, other):
        self.hours *= other
        self.minutes *= other
        self.seconds *= other
        return self


time1 = timeInterval(21, 58, 50)
time2 = timeInterval(1, 45, 22)
print(time1 * 2)