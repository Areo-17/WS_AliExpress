import random
list1 = []

missing_number = random.randint(1, 1000001)

for x in range (1, 1000001):
    if missing_number != x:
        list1.append(x)
