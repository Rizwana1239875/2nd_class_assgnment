# Python Operators:
# Python divides the operators in the following groups:
# 1 Arithmetic operators;
# 2 Assignment operators;
# 3 Comparisonoperators;
# 4 Logical operators
# 5 Identity operators
# 6 Membership operators
# 7 Bitwise operators


# 1 Arithmetic operators:


# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Addition(+) operators
x=6
y=8
print(x+y)

# Subtraction(-) operators
x=6
y=5
print(x-y)

# Multiplication(*) operators

x=4
y=2
print(x*y)

# Division(/) operators

x=6
y=2
print(x/y)

# Modulus(%) operators to get remainder in integer division
x=8   
y=3
print(x%y)

# Exponentiation(**) operators
x=5**2
print(x)

# Integer(//) division/Floor(//) division
x=5//2
print(x)
x=-5//2
print(x)

# 2 Assignment operators

# Assignment operators are used to assign values to variables:
# Assignment(=) operators

x = 4
print(x)

# Assignment(+=) operators

x += 4
print(x)

# Assignment(-=) operators

x -= 2
print(x)

# Assignment(*=) operators

x *= 2
print(x)

# Assignment(/=) operators

x /= 3
print(x)

# Assignment(%=) operators

x %= 2
print(x)

# Assignment(**=) operators
x = 12
x **= 2 # x = x
print(x)

# Assignment(//=) operators

x //= 2
print(x)

# 3 Comparisonoperators:

# Comparison operators are used to compare values. It returns Trus or False according to the condition.

# Equal(==) operators

x = 10
y = 5
print(x==y)

x = 10
y = 10
print(x==y)

# Not equal(!=) operators

x = 10
y = 20
print(x!=y)

# Greater than(>) operators

x = 10
y = 5
print(x>y)


# Less than(<) operators

x = 10
y = 5
print(x<y)

# Greater than or equal to(>=) operators

x = 10
y = 5
print(x>=y)

# Less than or equal to (<=) operators

x = 20
y = 20
print(x<=y)

# 4 Logical operators: 
# logical operators are used to combine conditional statements:
# and operator
# or operator
# not operator

x=10
y=20

print(x==10 and x<y )
print(x==10 or x<y or x==y)
print(not x!=10)


# 5 Identity operators:
# identity operators are used to compare the objects, not if they are equal, but if they are 
# actually the same object, with the same memory location:
# is operator
# is not operator

x=10
y=10
print(x is y, x==y)
print(x is not y,x!=y)


# 6 Membership operators:
# membership operators are used to test if a sequence is presented in an object:
# in operator
# not in operator

a = "Hello, World"
print("h" in a)
print("H" in a)

list=[10,20,30,40]
print(50 in list)
print(20 in list)

# 7 Bitwise operators:
# Bitwise operators are used to compare (binary) numbers it means 1=True,0=False:(and, or, xor, not, shift operators)
# & operator
# | operator
# ^ operator
# ~ operator
# << operator
# >> operator


a=10
b=8
print(bin(a))
print(bin(8))
print(bin(a&b))
print(a&b)
print(bin(a|b),a|b)
print(bin(a^b),a^ b)


#0b1010  (10 ka binary)
#0b1000   (8 ka binary)

#& 1000  8
#| 1010  10
#^ 0010  2








