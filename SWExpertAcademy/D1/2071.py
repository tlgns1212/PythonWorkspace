T = int(input())
for i in range(T):
    tenNums = list(map(int, input().split()))
    answer = 0
    for nums in tenNums:
        answer += nums
    answer /= 10
    print("#{} {}".format(i+1, round(answer)))
