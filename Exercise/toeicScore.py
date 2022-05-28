import random
a = []
for _ in range(8):
    a.append(1)
for _ in range(30):
    a.append(2)
for _ in range(40):
    a.append(3)
for _ in range(30):
    a.append(4)
for _ in range(30):
    a.append(5)
for _ in range(30):
    a.append(6)
for _ in range(20):
    a.append(7)
for _ in range(10):
    a.append(8)
for _ in range(2):
    a.append(9)
for _ in range(200):
    print(a[random.randint(0, 199)])
