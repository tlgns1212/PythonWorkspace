N = int(input())
for i in range(1, N+1):
    changed = False
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        changed = True
    for j in str(i):
        if '3' in j or '6' in j or '9' in j:
            print('-', end="")
        else:
            if changed == False:
                print(j, end="")
    print("", end=" ")
