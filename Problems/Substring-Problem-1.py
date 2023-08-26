'''

Given a string A and two integer B and C.

Find and return the substring of A starting from index B and ending with index C.

NOTE:

Consider 0 based indexing.
Try to use direct library function to solve this.

Example Input
Input 1:

 A = "rishabh"
 B = 1
 C = 2
Input 2:

 A = "ojas"
 B = 0
 C = 0


Example Output
Output 1:

 "is"
Output 2:

 "o"

'''


#Solution
originalString = input("Enter a String: ")
lenOfString = len(originalString)
print("enter the start number between 0 to", lenOfString)
a = int(input())
print("enter the end number between 0 to", lenOfString)
b = int(input())
subString = originalString[a:b]
print(subString)