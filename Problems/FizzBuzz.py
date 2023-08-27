'''

Problem Description:

Given a positive integer A, return an array of strings with all the integers from 1 to N. 
But for multiples of 3 the array should have “Fizz” instead of the number. For the multiples of 5, 
the array should have “Buzz” instead of the number. For numbers which are multiple of 3 and 5 both, 
the array should have "FizzBuzz" instead of the number.



Example Input
Input 1:

 A = 5

Example Output
Output 1:

 [1 2 Fizz 4 Buzz]

'''

def fizzBuzz(A):
    arr = []
    for i in range(1, A+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FizzBuzz")
        elif i % 3 == 0:
            arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(str(i))
    return arr

print(fizzBuzz(5))











