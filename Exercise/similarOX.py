# import random
# for _ in range(200):
#     print(random.randint(0, 1))
#
import random
a = []
for _ in range(54):
    a.append(0)
for _ in range(110):
    a.append(1)
for _ in range(20):
    a.append(2)
for _ in range(10):
    a.append(3)
for _ in range(5):
    a.append(4)
for _ in range(1):
    a.append(5)
for _ in range(200):
    print(a[random.randint(0, 199)])
