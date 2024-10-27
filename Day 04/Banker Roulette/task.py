import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0, 4)
if random_index == 0:
    print(friends[0])
if random_index == 1:
    print(friends[1])
if random_index == 2:
    print(friends[2])
if random_index == 3:
    print(friends[3])
if random_index == 4:
    print(friends[4])

# Angela's solutions
# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])