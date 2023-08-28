'''
to print 
    ####
    ####
    ####
    ####
''' 

n = int(input("Enter no. of hashes per row: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print("#", end="")
    print();
