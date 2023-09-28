"""
=> @auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#A - Power Of Two
import math
n = int(input())
res = math.log(n,2)
if res == int(res):
    print("YES")
else:
    print("NO")
