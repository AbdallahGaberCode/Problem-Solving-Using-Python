"""
=> @auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#E - Maximum Distinct Numbers
num = int(input())
i = 1
while True:
    if i > num:
        print(i-1)
        break
    else:
        num -= i
    i+=1
