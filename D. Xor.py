"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#D. Xor
lst =[int(x) for x in input().split()]
a=lst[0]
b=lst[1]
q=lst[2]
Qth = q%3
if Qth == 1:
    print(a)
elif Qth == 2:
    print(b)
else:
    print((a ^ b))
