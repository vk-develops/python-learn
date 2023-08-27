def year(A):
    if A % 400 == 0:
         return 1
    elif A % 4 == 0 and A % 100 != 0:
         return 1
    return 0

print(year(2002))