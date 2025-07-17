# mymodule.py

def myadd(*args):
    return sum(args)

def mysub(*args):
    if len(args) < 2:
        return "Need at least two numbers"
    result = args[0]
    for i in args[1:]:
        result -= i
    return result

def mymul(*args):
    result = 1
    for i in args:
        result *= i
    return result

def mydiv(*args):
    if len(args) < 2:
        return "Need at least two numbers"
    result = args[0]
    for i in args[1:]:
        if i == 0:
            return "Division by zero error"
        result /= i
    return result

def mymodulo(*args):
    return args[0] % args[1] if len(args) >= 2 else "Need 2 arguments"

def myAND(*args):
    result = args[0]
    for i in args[1:]:
        result &= i
    return result

def myOR(*args):
    result = args[0]
    for i in args[1:]:
        result |= i
    return result

def myXOR(*args):
    result = args[0]
    for i in args[1:]:
        result ^= i
    return result

def mySquare(a): return a * a
def myCube(a): return a * a * a
def mySqrt(a): return a ** 0.5
def myCbrt(a): return a ** (1/3)
def myexpo(a,b): return a ** b

def myfact(a):
    if a < 0: return "No factorial for negatives"
    result = 1
    for i in range(1, a + 1): result *= i
    return result

def mypercent(a,b): return (a/b) * 100 if b != 0 else "Division by zero"
