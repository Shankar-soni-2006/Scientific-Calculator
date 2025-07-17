import mymodule

def get_numbers():
    nums = input("Enter numbers separated by space: ").split()
    return [int(i) for i in nums]

def get_two_numbers():
    nums = input("Enter two numbers (a b): ").split()
    return int(nums[0]), int(nums[1])

def get_one_number():
    return int(input("Enter one number: "))

def main():
    print("=== Calculator with Arbitrary Arguments ===")
    print("Select category:")
    print("1. Arithmetic (+, -, *, /, modulo, percent, exponent)")
    print("2. Logical (AND, OR, XOR)")
    print("3. Root/Power (Square, Cube, Sqrt, Cbrt)")
    print("4. Other (factorial)")

    category = input("Enter category number: ")

    if category == "1":
        print("Available ops: +, -, *, /, modulo, percent, exponent")
        op = input("Enter operation: ")
        if op == "percent" or op == "exponent" or op == "modulo":
            print("Enter the two numbers")
            a, b = get_two_numbers()
            match op:
                case "percent":
                    print("Result:", mymodule.mypercent(a,b))
                case "exponent":
                    print("Result:", mymodule.myexpo(a,b))
                case "modulo":
                    print("Result:", mymodule.mymodulo(a,b))
        else:
            nums = get_numbers()
            match op:
                case "+":
                    print("Result:", mymodule.myadd(*nums))
                case "-":
                    print("Result:", mymodule.mysub(*nums))
                case "*":
                    print("Result:", mymodule.mymul(*nums))
                case "/":
                    print("Result:", mymodule.mydiv(*nums))
                case _:
                    print("Invalid operation")

    elif category == "2":
        print("Available logical ops: AND, OR, XOR")
        op = input("Enter operation: ")
        nums = get_numbers()
        match op:
            case "AND":
                print("Result:", mymodule.myAND(*nums))
            case "OR":
                print("Result:", mymodule.myOR(*nums))
            case "XOR":
                print("Result:", mymodule.myXOR(*nums))
            case _:
                print("Invalid operation")

    elif category == "3":
        print("Available: Square, Cube, Sqrt, Cbrt")
        op = input("Enter operation: ")
        # print("Enter one number")
        a = get_one_number()
        match op:
            case "Square":
                print("Result:", mymodule.mySquare(a))
            case "Cube":
                print("Result:", mymodule.myCube(a))
            case "Sqrt":
                print("Result:", mymodule.mySqrt(a))
            case "Cbrt":
                print("Result:", mymodule.myCbrt(a))
            case _:
                print("Invalid operation")

    elif category == "4":
        op = input("Enter operation (factorial): ")
        a = get_one_number()
        if op == "factorial":
            print("Result:", mymodule.myfact(a))
        else:
            print("Invalid operation")
    else:
        print("Invalid category")

main()
