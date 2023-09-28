"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#C. sum of Range
def sum_all(n):
    return n*(n+1)//2
def sum_even(n):
    return n//2 * (n//2 +1)
def sum_odd(n):
    res = (n+1)//2
    res = res*res
    return res
lst = [int(x) for x in input().split()]
lst = sorted(lst,reverse=True)  #to make the bigger number first

num1 =lst[0]
num2 =lst[1] -1 #smaller number -1 bcz we count smaller number itself.

print(sum_all(num1) - sum_all(num2))
print(sum_even(num1) - sum_even(num2))
print(sum_odd(num1) - sum_odd(num2))
