N = int(input())
for i in range(1, N+1):
    changed = False                                     # -가 있는지 확인용
    if '3' in str(i) or '6' in str(i) or '9' in str(i):  # 3,6,9가 있으면 숫자 출력 불가
        changed = True
    for j in str(i):                                    # 모든 문자를 비교
        if '3' in j or '6' in j or '9' in j:            # 3,6,9가 있으면 -하나 출력
            print('-', end="")
        else:
            if changed == False:                        # 문자열에 3,6,9가 하나라도 있으면 숫자 출력 불가
                print(j, end="")
    print("", end=" ")
