"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#B - Prime checking
import math
n = int(input())
if n == 2:
    print('YES')
    quit()
if n == 1 or n == 0:
    print("NO")
    quit()
prime = 1
for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        prime = 0
        break
if prime:
    print("YES")
else:
    print("NO")
