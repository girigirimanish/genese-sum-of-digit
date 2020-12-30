# Function which returns the sum of the factorial of the provided number.
def sum_of_factorial_of_this_digit(n):
   n = factorial(n)
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

# Function which returns the factorial of a number.
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# Lets print out the sum of the 
print(sum_of_factorial_of_this_digit(10))