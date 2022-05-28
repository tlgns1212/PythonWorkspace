import random
a = []
# for _ in range(50):
#     a.append(1)
# for _ in range(40):
#     a.append(2)
# for _ in range(40):
#     a.append(3)
# for _ in range(30):
#     a.append(4)
# for _ in range(30):
#     a.append(5)
# for _ in range(10):
#     a.append(6)
# for _ in range(200):
#     print(a[random.randint(0, 199)])
soon = []
for _ in range(200):
    soon.append(int(input()))
for i in range(200):
    if soon[i] == 1:
        a.append(random.randint(3, 6))
    elif soon[i] == 2:
        a.append(random.randint(2, 6))
    elif soon[i] == 2:
        a.append(random.randint(2, 5))
    elif soon[i] == 3:
        a.append(random.randint(1, 5))
    elif soon[i] == 4:
        a.append(random.randint(1, 4))
    elif soon[i] == 5:
        a.append(random.randint(1, 4))
    elif soon[i] == 6:
        a.append(random.randint(1, 3))
    elif soon[i] == 7:
        a.append(random.randint(1, 2))
    elif soon[i] == 8:
        a.append(random.randint(1, 1))
    elif soon[i] == 9:
        a.append(random.randint(1, 1))
print('\n\n\n\n\n\n\n\n\n\n\n')
for i in range(200):
    print(a[i])
