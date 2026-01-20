def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    def reset():
        helper.calls = 0

    helper.calls = 0
    helper.reset = reset
    return helper

@call_counter
def factorial(n):
    if n == 0 or n == 1: return 1
    else: return n * factorial(n - 1)

n = input("Enter the factorial number: ")
n = int(n)

result = factorial(n)
print(f"The factorial of {n} is {result}")
print(f"Complexity: {factorial.calls} calls")
factorial.reset()

