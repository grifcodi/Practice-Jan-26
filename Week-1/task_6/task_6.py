
def factorial(n):
    if n == 0 or n == 1: return 1
    else: return n * factorial(n - 1)

fact = input("Enter the factorial number: ")
fact = int(fact)
print(factorial(fact))