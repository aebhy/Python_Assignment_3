#calculate factorial using a function
num_1=int(input("Enter a number: "))
def factorial(num_1):
    if num_1 < 2:
        return 1
    else:
        return num_1 * factorial(num_1 - 1)

result = factorial(num_1)
print(f"The factorial of {num_1} is: {result}") 