T = int(input())
for i in range(T):
    A = list(map(int, input().split()))
    sum = 0
    for num in A:
        if num % 2 == 1:
            sum += num
    print("#{0} {1}".format(i+1, sum))
