import random
# random_number_0_to_1 = random.random()*10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1,10)
# print(random_float)
random_number_0_to_1 = round(random.random()*10)
if random_number_0_to_1 >=5:
    print("Heads")
else:
    print("Tails")

#solution by Angela
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
