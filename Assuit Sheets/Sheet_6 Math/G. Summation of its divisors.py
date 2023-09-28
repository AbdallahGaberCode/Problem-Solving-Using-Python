"""
=> @auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
import math
n = int(input())
count =0
k=int(math.sqrt(n))  
for i in range(1,k+1):  #we add 1 for the k bcz we need to k itself so we add 1 to the end
    if n %i ==0:
        count += i
        if i != k or i != n//i:
            count += (n//i)
print(count)
