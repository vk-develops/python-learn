# Problem statement: 

# To find the largest element in the array with and without using functions

arr = [20, 50, 30, 10, 40]

## Without Function
def withOutFunction():

    highest = arr[0]

    for i in arr:
        if i > highest:
            highest = i

    return highest

print("Highest without function is: ", withOutFunction())
print()

# With function

highest = max(arr)
print("Highest with function is: ", highest)