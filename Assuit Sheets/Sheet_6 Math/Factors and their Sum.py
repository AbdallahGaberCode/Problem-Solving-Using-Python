"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
# Number Factors and their sum
import math
n = int(input())
k = int(math.sqrt(n))
factors=[]
for i in range(1,k+1):
    if n % i==0:
        factors.append(i)
        if i != k or i != n//i:
            factors.append(n//i)
for item in factors:
    print(item,end=' ')
print()
print(sum(factors))
