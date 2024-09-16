class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high


    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Counter(1, 5)
for number in counter:
    print(number)

counter = Counter(1, 5)
print(next(counter))


def get_next_value():
    try:
        return next(counter)
    except StopIteration:
        return 'Completed - end of counter'
