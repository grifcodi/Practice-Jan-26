

def quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    D =  b**2 - 4*a*c

    if D < 0:
        return "No solution"
    elif D == 0:
        x = -b/(2*a)
        print("x = ", x)
        return x
    elif D > 0:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        return x1, x2

    return None


inp_a, inp_b, inp_c = input("Enter a, b, c: ").split()
print(quadratic(inp_a, inp_b, inp_c))