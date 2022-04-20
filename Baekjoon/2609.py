import sys
import math
A, B = map(int, sys.stdin.readline().split())
print('{0}\n{1}'.format(math.gcd(A, B), math.lcm(A, B)))
