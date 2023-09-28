"""
@auther:Abdallah_Gaber
=> A computer science student
=> AOU University "Egypt Branch"
"""
#shaass and osklas problem
n = int(input())
birds = [int(x) for x in input().split()]
m = int(input())
for i in range(m):
    lst = [int(x) for x in input().split()]
    x = lst[0]
    y = lst[1]
    x -= 1

    if x != 0:
        birds[x-1] += y-1

    if x != len(birds)-1:
        birds[x+1] += birds[x]-y
    birds[x] = 0
for item in birds:
    print(item)
