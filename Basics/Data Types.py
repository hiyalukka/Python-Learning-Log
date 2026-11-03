# 1. The core built-in types, and how to check one with type()
print(type(42))              # Output: <class 'int'>
print(type(3.14))            # Output: <class 'float'>
print(type("hi"))            # Output: <class 'str'>
print(type(True))            # Output: <class 'bool'>
print(type(None))            # Output: <class 'NoneType'>
print(type(3 + 4j))          # Output: <class 'complex'>

# 2. int has no size limit (Python switches to big integers automatically)
print(2 ** 100)              # Output: 1267650600228229401496703205376
# KEY: no overflow in Python ints, unlike C or Java.

# 3. float is approximate, because it is stored in binary
print(0.1 + 0.2)             # Output: 0.30000000000000004
print(0.1 + 0.2 == 0.3)      # Output: False
# GOTCHA: never compare floats with ==. Use math.isclose() or round().
import math
print(math.isclose(0.1 + 0.2, 0.3))   # Output: True
print(round(0.1 + 0.2, 2))            # Output: 0.3

# 4. str is immutable: methods return a NEW string, the original stays
s = "hello"
print(s.upper())             # Output: HELLO
print(s)                     # Output: hello
try:
    s[0] = "H"
except TypeError as e:
    print(type(e).__name__)  # Output: TypeError
# GOTCHA: s.upper() alone does nothing to s. You must write s = s.upper().

# 5. bool is a subclass of int: True is 1 and False is 0
print(True + True)           # Output: 2
print(isinstance(True, int)) # Output: True

# 6. None means "no value here". Check it with `is`, not ==
result = None
print(result is None)        # Output: True
# KEY: a function with no return statement gives back None.

# 7. Type conversion (casting): int(), float(), str(), bool()
print(int("42"))             # Output: 42
print(float("3.5"))          # Output: 3.5
print(str(10) + "!")         # Output: 10!
print(int(3.9))              # Output: 3
print(int(-3.9))             # Output: -3
# GOTCHA: int() truncates toward zero, it does not round. Use round() to round.
try:
    int("3.5")
except ValueError as e:
    print(e)                 # Output: invalid literal for int() with base 10: '3.5'
# GOTCHA: int("3.5") fails. Go through float first: int(float("3.5")).

# 8. Truthiness: these are all False when used as a condition
print(bool(0), bool(""), bool([]), bool(None))   # Output: False False False False
print(bool("0"), bool(" "))                      # Output: True True
# GOTCHA: the string "0" is True, because only an EMPTY string is False.
# WHY: any non-empty container or non-zero number counts as True.

# 9. isinstance() checks a type, and accepts a tuple of types
print(isinstance(5, (int, float)))   # Output: True
print(isinstance("5", int))          # Output: False

# 10. complex numbers have a real and an imaginary part
z = 3 + 4j
print(z.real, z.imag)        # Output: 3.0 4.0
print(abs(z))                # Output: 5.0


