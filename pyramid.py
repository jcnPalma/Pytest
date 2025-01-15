import random

heigth = random.randrange(5, 10)
widht = heigth + 1

for i in range(heigth):
    print(" " * (widht - i) + "*" * (2 * i + 1))