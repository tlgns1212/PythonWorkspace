import random
cast = []
sim = []
best = []

print("다음")
for _ in range(200):
    cast.append(int(input()))
print("다음")
for _ in range(200):
    sim.append(int(input()))
print("다음")
for _ in range(200):
    best.append(int(input()))

min = 20
max = 40
min1 = 0
max1 = 0
answer = []
for i in range(200):
    if cast[i] == 1:
        if sim[i] == 1:
            if best[i] == 1:                            # 1등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 1등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 2:
        if sim[i] == 1:
            if best[i] == 1:                            # 2등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 2등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 3:
        if sim[i] == 1:
            if best[i] == 1:                            # 3등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 3등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 4:
        if sim[i] == 1:
            if best[i] == 1:                            # 4등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 4등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 5:
        if sim[i] == 1:
            if best[i] == 1:                            # 5등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 5등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 6:
        if sim[i] == 1:
            if best[i] == 1:                            # 6등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 6등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 7:
        if sim[i] == 1:
            if best[i] == 1:                            # 7등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 7등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 8:
        if sim[i] == 1:
            if best[i] == 1:                            # 8등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 8등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
    elif cast[i] == 9:
        if sim[i] == 1:
            if best[i] == 1:                            # 9등급, 토익O, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
        elif sim[i] == 0:
            if best[i] == 1:                            # 9등급, 토익X, 집중 1시간
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 2:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 3:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 4:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 5:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))
            elif best[i] == 6:
                min1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                max1 = min + (cast[i] * 20) + \
                    (30 if sim[i] else 5) - (best[i] * 5)
                answer.append(random.randint(min1, max1))

for i in range(200):
    print(answer[i])
