class CachedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        self.cache.append(next(self.iterator))
        return self.cache[-1]

    def __getitem__(self, query):
        return self.cache[query]


if __name__ == "__main__":
    c = CachedIterator(i**2 for i in range(20))

    for _ in range(5):
        print(next(c))

    print("---")

    print(c[3])
    print(next(c))
    print(next(c))

    print("---")

    for x in c:
        print(x)
