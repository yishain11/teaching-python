# map
nums = [1, 2, 3, 4]


def f(val):
    pass


doubles = map(f, nums)
print(list(doubles))

# filter
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))
