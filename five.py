import math
a = int(input())
print(abs(math.ceil(a / 5) - a // 5 - 1))