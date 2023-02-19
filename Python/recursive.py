# A function for computing Fibonacci numbers
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
# Let's call the 1000th Fibonacci number:
print(fibonacci(1000))