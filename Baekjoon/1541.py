import sys
import re
givenNum = sys.stdin.readline().strip()     # 입력값
signs = []
for i in range(len(givenNum)):
    if not givenNum[i].isnumeric():         # 부호만 따로 분류
        signs.append(givenNum[i])
nums = re.split('[+|-]', givenNum)          # 숫자끼리 분류
nums = list(map(int, nums))
answer = nums[0]
temp = 0
i = 0
isAdded = False
while(i < len(signs)):
    if signs[i] == '-':                     # 부호가 '-'인데
        for j in range(i+1, len(signs)):
            if signs[j] == '-':             # 다음 부호도 '-'이면
                answer -= (nums[j])
                isAdded = False
                break
            else:                           # 다음 부호도 '+'이면
                nums[j+1] += (nums[j])
                i += 1
                isAdded = True
        if isAdded:                         # 부호가 '-+++'와 같이 '-'가 다시 나타나지 않으면
            answer -= nums[i+1]
            isAdded = False
    else:                                   # 부호가 '+'이면
        answer += (nums[i+1])
    if i == len(signs)-1 and signs[i] == '-':   # 마지막 부호가 '-'이면
        answer -= nums[i+1]
    i += 1
print(answer)
