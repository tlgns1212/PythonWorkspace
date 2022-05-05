import sys
import re
givenNum = sys.stdin.readline().strip()
signs = []
for i in range(len(givenNum)):
    if not givenNum[i].isnumeric():
        signs.append(givenNum[i])
nums = re.split('[+|-]', givenNum)
nums = list(map(int, nums))
# 1. no minus           : add it all
# 2. minus with plus    : before minus, no brackets, after minus, bracket all before minus
# 3. only minus         : add it all
answer = nums[0]
temp = 0
i = 0
isAdded = False
while(i < len(signs)):
    if signs[i] == '-':
        for j in range(i+1, len(signs)):
            if signs[j] == '-':
                answer -= (nums[j])
                isAdded = False
                break
            else:
                nums[j+1] += (nums[j])
                i += 1
                isAdded = True
        if isAdded:
            answer -= nums[i+1]
            isAdded = False
    else:
        answer += (nums[i+1])
    if i == len(signs)-1 and signs[i] == '-':
        answer -= nums[i+1]
    i += 1
print(answer)
