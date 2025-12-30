class Worker:
    def __init__(self, hourly_rate) -> None:
        self.hours = 0
        self.hourly_rate = hourly_rate

    def calc_salary(self):
        return self.hours * self.hourly_rate


w = Worker(20)

# bad - access to internal hours
# print(w.calc_salary())

# w.hours = 1000

# print(w.calc_salary())

# better - set as private


class SafeWorker:
    def __init__(self, hourly_rate) -> None:
        self.__hours = 0
        self.__hourly_rate = hourly_rate

    def calc_salary(self):
        return self.__hours * self.__hourly_rate


w1 = SafeWorker(20)
print(w1.__dict__)
print(w1.calc_salary())

w1.__hours = 1000
print("hours", w1.__hours)
print(w1.calc_salary())
