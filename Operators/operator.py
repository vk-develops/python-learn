a = 10
b = 20
arr = [1, 2, 3]

# if a == 10 & a < b:
#     print("True")


# for i in range(0, len(arr)):
#     if i == 2:
#         print("True")


# print(6 % 2)
# print( 2 >3 and 4< 2)


def solve(A, B):
    return A + B

print(solve("interveiw", "Bit"))


def volume_sphere(r):
    '''input: r = Input in integer format
       output:return Vol of sphere upto two decimals'''
    # YOUR CODE GOES HERE
    Vol=None
    
    pi = 22/7
    Vol = (4*pi*(r^3))/3
    
    return Vol

print(volume_sphere(8))