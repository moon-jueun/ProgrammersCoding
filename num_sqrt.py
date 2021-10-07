import math
n = 3
num_sqrt = math.sqrt(n)
answer = 0
if n/num_sqrt**2 == 1.0:
    answer = int((num_sqrt+1)**2)
else:
    answer = -1

print(answer)