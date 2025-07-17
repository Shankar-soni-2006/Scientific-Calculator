# Scientific-Calculator
🧮 Multi-Operation CLI Calculator (Python)
This is a command-line calculator built in Python that performs Arithmetic, Logical, Root/Power, and Other operations like factorial. It uses a modular approach with a separate mymodule.py containing all the computation logic.
calculator/
│
├── main.py         # User interface logic
├── mymodule.py     # Core calculation functions
└── README.md       # Project documentation
🚀 How to Run
Make sure you have Python installed (preferably 3.x).

Clone or download the files into a folder.

Run the program:
python main.py
🧩 Features
1. Arithmetic Operations
Add (+)

Subtract (-)

Multiply (*)

Divide (/)

Modulo (modulo)

Percentage (percent)

Exponentiation (exponent)

2. Logical Operations
AND

OR

XOR

3. Root/Power Operations
Square

Cube

Square Root

Cube Root

4. Other
Factorial

🛠️ Module Functions
Arithmetic (mymodule.py)
Function	Description
myadd(*args)	Adds any number of values
mysub(*args)	Subtracts values from left to right
mymul(*args)	Multiplies all values
mydiv(*args)	Divides left to right, with zero check
mymodulo(a, b)	Returns a % b
mypercent(a, b)	Calculates (a / b) * 100
myexpo(a, b)	Returns a ** b

Logical
Function	Description
myAND(*args)	Bitwise AND
myOR(*args)	Bitwise OR
myXOR(*args)	Bitwise XOR

Root/Power
Function	Description
mySquare(a)	Square of a
myCube(a)	Cube of a
mySqrt(a)	Square root of a
myCbrt(a)	Cube root of a

Other
Function	Description
myfact(a)	Factorial of a

📋 Input Format
The program uses input() to get user values.

Multiple values: space-separated numbers.

Some operations require only one or two inputs.

