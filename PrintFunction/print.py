# Printing multiple elements in a print function
print("Rdj", "Hemsworth", "Evans", 26, 28, 30, 99.90, 88.50, 75.90)

print("/****************************************************/")


'''
Changing the space seperator of the multiple print values
using the sep attribute of the print function
'''

#Using Comma(,) as a seperator instead of space for seperating the values
print("Rdj", "Hemsworth", "Evans", 26, 28, 30, 99.90, 88.50, 75.90, sep=",")

#Using new line("\n") as a seperator instead of space for seperating the values
print("Rdj", "Hemsworth", "Evans", sep="\n")


print("/****************************************************/")


#multiple prints without end attribute
print("Rdj")
print("Hemsworth")
print("Evans")


'''
multiple prints are printed column wise by the inbuilt end="" attribute....
Changing the column wise print using end attribute
'''



print()
#Printing multiple prints in same line
print("Rdj", end=" ")
print("Hemsworth", end=" ")
print("Evans", end=" " )
print()
print()

#Printing multiple prints in same line with a symbol
print("Rdj", end="->")
print("Hemsworth", end="->")
print("Evans", end="->" )
print()
print()