T = int(input())
for i in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    max = days[-1]
    money = 0
    for j in range(len(days)-1, -1, -1):
        if max < days[j]:
            max = days[j]
        else:
            money += max - days[j]
    print("#{} {}".format(i+1, money))
