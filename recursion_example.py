# taking input
n = int(input("enter a number:"))
initial_number = 0

# funtion to calculate sum of n whole number
def add_again(number):
    global initial_number
    initial_number += number
    if number>0:
        add_again(number-1)

    return initial_number

# calling the function
print(add_again(n))
