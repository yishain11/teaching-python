class My_Iterator:
    def __init__(self, values) -> None:
        self.index = 0
        self.values = values
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.values):
            value = self.values[self.index]
            self.index += 1
            return value
        raise StopIteration


my_iter = My_Iterator([5, 4, 3])

for n in my_iter:
    print(n)


# with more interesting logic


# show only words with more than 5 letters, not starting with a - and show them with upper case
class Filter_Words_Iter:
    def __init__(self, words) -> None:
        self.index = 0
        self.words = words

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if len(word) > 5 and not word.startswith("-"):
                return word.upper()
        raise StopIteration


words = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti hic mollitia dolorem provident necessitatibus ipsam consectetur. Similique fugiat dolor, dicta architecto nam aliquid repellendus sequi recusandae explicabo numquam velit deleniti atque, dolorem modi, consectetur fuga. Aliquid aut animi ex atque tempore quos, veritatis eius eum voluptas numquam molestias suscipit excepturi?".split(
    " "
)
filter_words = Filter_Words_Iter(words)
for word in filter_words:
    print(word)


# generators
def filter_words_gen(words):
    for word in words:
        if len(word) > 5 and not word.startswith("-"):
            yield word.upper()


for word in filter_words_gen(words):
    print(word)


# yield sum from 2 diff lists


def sum_2_values(l1, l2):
    for val1 in l1:
        for val2 in l2:
            yield val1 + val2


for sum in sum_2_values([1, 2, 3], [4, 5]):
    print("sum", sum)
