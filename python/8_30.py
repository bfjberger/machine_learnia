import math
import random
import statistics
import os
import glob

list = [4, 6, 9, 18, 67, 90]
# print(math.cos(2*math.pi))
# print(math.exp(5))

# print(statistics.mean(list))
# print(statistics.variance(list))

random.seed(0)
print(random.choice(['jean', 'anne', 'julie']))
print(random.random())
print(random.randint(5, 10))
print(random.randrange(100))

print(random.sample(range(100), 10))
print(random.sample(range(100), random.randrange(10)))

random.shuffle(list)
print(list)

print(os.getcwd())

print(glob.glob("*"))