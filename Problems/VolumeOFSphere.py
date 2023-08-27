'''

Problem Description:

You are given a positive integer r denoting the radius of a sphere as a parameter. Write a program to calculate the volume of the sphere. The volume of a sphere having radius R is given by (4 * π * R3) / 3.

NOTE: Return the volume of the sphere up to two decimal places. You can use round().

NOTE2: Use pi as 22/7 (not math.pi).

Sample Input:

1
8
Sample Output:

2145.52

'''

#Program

def volumeOfSphere(rad):
    pi = 22/7
    Volume = (4*pi*(rad**3)/3)
    rounded = round(Volume, 2)
    print(rounded)

volumeOfSphere(8)