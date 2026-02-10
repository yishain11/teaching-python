# create list with nums fomr 5-15

l1 = []
for i in range(5, 15):
    l1.append(i)

print(l1)

# with comp

l1 = [x for x in range(5, 15)]

# create list with nums from 0-500 only evens
l1 = []
for i in range(500):
    if i % 2 == 0:
        l1.append(i)

print(l1)

# with comp
l1 = [x for x in range(500) if x % 2 == 0]

# double values
l1 = [x * 2 for x in range(10)]
