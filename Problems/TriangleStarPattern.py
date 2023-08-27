'''

Triangle Star- Pattern
Problem Description:

Write a function to print the pattern shown in the sample using n given as a parameter, where n defines the number of rows.

Note: There isn't any space between consecutive stars.




Sample Input:

5
Sample Output:

    *
   ***
  *****
 *******
*********

'''

#Program
def print_pattern(rows):
    for i in range(1, rows + 1):
        spaces = rows - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

rows = 5  
print_pattern(rows)