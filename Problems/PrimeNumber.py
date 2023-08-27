'''

Prime finder
Write a function to return True when the given function is a Prime number else False.



Input sample

5
Input format

True

'''


#Program
def solve(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True
    return False  

print(solve(1))