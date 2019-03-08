# https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
import inspect


class Averager:
    def __init__(self):
        # [1]
        print('> ', inspect.currentframe().f_code.co_name)
        # [2]
        print('> ', inspect.stack()[0][3])
        self.series = []

    def __call__(self, new_value):
        print('> ', inspect.stack()[0][3])
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

