"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
# GCD Ecludis algorithm
def GCD(a,b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a
def LCM(a,b):
    return(a//GCD(a,b))*b  #this law to get the LCM using the GCD of two numbers

lst = [int(x) for x in input().split()]
lst = sorted(lst,reverse=True)
a = lst[0]
b = lst[1]
print(GCD(a,b),LCM(a,b))
