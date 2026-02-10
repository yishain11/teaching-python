import sys

N = 1_000_000

# LIST VERSION
list_nums = [x * x for x in range(N)]

# GENERATOR VERSION
gen_nums = (x * x for x in range(N))

print("List memory:", sys.getsizeof(list_nums))
print("Generator memory:", sys.getsizeof(gen_nums))


# option 1
# for i, num in enumerate(range(5)):
#     if i % 3 == 0:
#         print(num)


class My_List:
    def __init__(self, values) -> None:
        self.values = values
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.values) <= self.current_index:
            raise StopIteration
        value = self.values[self.current_index]
        self.current_index += 3
        return value


big_list = [x for x in range(100_000_000)]
my_list_1 = My_List(big_list)

# for num in my_list_1:
#     print(num)

def gen_from_list(values):
    i = 0
    n = len(values)
    while i < n:
        yield values[i]
        i += 3


# better memory
class My_List_Better_Mem:
    def __init__(self, max) -> None:
        self.max = max
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max <= self.current_num:
            raise StopIteration
        value = self.current_num
        self.current_num += 3
        return value


l_with_mem = My_List_Better_Mem(100_000_000)
# for num in l_with_mem:
#     print(num)

def gen_better_mem(max):
    current = 0
    while current < max:
        yield current
        current += 3

gen_list_iter = gen_from_list(big_list)
gen_better_iter = gen_better_mem(100_000_000)

import sys

print("big list", sys.getsizeof(big_list))
print("l_with_mem", sys.getsizeof(l_with_mem))
print("my_list_1", sys.getsizeof(my_list_1))
print("my_list_1 vals", sys.getsizeof(my_list_1.values))
print("gen_list_iter", sys.getsizeof(gen_list_iter))
print("gen_better_iter", sys.getsizeof(gen_better_iter))
