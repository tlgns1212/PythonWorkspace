import sys
word = sys.stdin.readline().strip()     # 받는 문자열
alphas = [0 for _ in range(27)]         # 알파벳 개수
odds = 0                                # 홀수 개수
oddIndex = -1                           # 홀수의 위치
for letters in word:
    alphas[ord(letters)-65] += 1
for i in range(len(alphas)):
    if alphas[i] % 2 == 1:
        odds += 1
        oddIndex = i
        if odds == 2:                   # 홀수가 2개 이상이면
            print("I'm Sorry Hansoo")
            exit()
alphas[oddIndex] -= 1                   # 홀수의 알파벳 하나 미리 빼놓기
for i in range(len(alphas)):            # 팰린드롬의 좌측 출력
    if alphas[i] % 2 != 1:
        for _ in range(alphas[i]//2):
            print(chr(i+65), end="")
if oddIndex != -1:
    print(chr(oddIndex+65), end="")     # 미리 빼놓은 알파벳 하나 출력
for i in range(len(alphas)-1, -1, -1):  # 팰린드롬의 우측 출력
    if alphas[i] % 2 != 1:
        for _ in range(alphas[i]//2):
            print(chr(i+65), end="")
