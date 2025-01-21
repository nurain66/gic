# Take the inputs of a and b
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
    
# A loop to find the greatest common divisor
while b != 0:
    placeholder = b
    b = a % b
    a = placeholder

# Printing the greatest common divisor
print(f"The greatest common divisor is {a}")