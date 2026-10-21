import random

requirements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

requirement1 = random.choice(requirements)
requirements.remove(requirement1)
requirement2 = random.choice(requirements)
print("Your requirements are: ", requirement1, "and",requirement2)