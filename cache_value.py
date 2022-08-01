from random import randint

class Cache:
    def __init__(self):
        self.__values = dict()
        self.__times_called = 0
    
    def caching(self, func):
        def wrapper(value):
            self.__times_called += 1
            if value not in self.__values:
                self.__values[value] = func(value)
            return self.__values[value]
        return wrapper
    
    def cache(self, key=None):
        return self.__values[key] if key else self.__values

    @property
    def times_ignore(self):
        return abs(len(self.__values) - self.__times_called)

    @property
    def times_cached(self):
        return len(self.__values)

    def __str__(self):
        return str(self.__values)



util = Cache()


@util.caching
def calc(x):
    return x*x + 1


if __name__ == '__main__':
    [calc(randint(1, 10)) for i in range(100)]
    print(f'Cache: {util}')
    print(f'{util.times_cached = }')
    print(f'{util.times_ignore = }')
    print(util.cache(1))