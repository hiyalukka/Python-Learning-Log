# 1. Arithmetic operators: + - * / // % **
print(7 + 2, 7 - 2, 7 * 2)   # Output: 9 5 14
print(7 / 2)                 # Output: 3.5
print(7 // 2)                # Output: 3
print(7 % 2)                 # Output: 1
print(2 ** 3)                # Output: 8
# KEY: / is true division, // is floor division, % is the remainder, ** is power.

# 2. / ALWAYS gives a float, even when it divides evenly
print(6 / 3)                 # Output: 2.0
print(7.5 // 2)              # Output: 3.0
# GOTCHA: use // when you need an int result, otherwise you get 2.0 not 2.

# 3. Floor division rounds DOWN, so negatives go the other way
print(-7 // 2)               # Output: -4
print(-7 % 2)                # Output: 1
# GOTCHA: -7 // 2 is -4, not -3. Floor means toward negative infinity.
# WHY: Python keeps (a // b) * b + (a % b) == a, so % follows the floor.
print(divmod(7, 2))          # Output: (3, 1)

# 4. Comparison operators: == != < > <= >=
print(5 == 5.0)              # Output: True
print(5 != 6)                # Output: True
# KEY: == compares values, `is` compares identity (the same object).
a = [1]
b = [1]
print(a == b)                # Output: True
print(a is b)                # Output: False

# 5. Chained comparisons read like maths
print(1 < 5 < 10)            # Output: True
print(1 < 5 > 10)            # Output: False
# KEY: 1 < 5 < 10 means (1 < 5) and (5 < 10). No need to write `and`.

# 6. and / or / not return one of their OPERANDS, not just True or False
print(0 or "default")        # Output: default
print("hi" and 5)            # Output: 5
print(not 0)                 # Output: True
# KEY: `or` returns the first truthy value, `and` returns the first falsy one (or the last value).
# WHY: that's what makes `name = user_input or "guest"` work as a default.

# 7. Short-circuit: the right side is skipped when the left already decides the answer
print(False and 1 / 0)       # Output: False
# KEY: no ZeroDivisionError here, because 1 / 0 never runs.

# 8. Assignment operators: += -= *= /= //= %= **=
x = 10
x += 5
print(x)                     # Output: 15
x //= 2
print(x)                     # Output: 7
x **= 2
print(x)                     # Output: 49

# 9. Precedence: ** first, then * / // %, then + -
print(2 + 3 * 4)             # Output: 14
print((2 + 3) * 4)           # Output: 20
print(-2 ** 2)               # Output: -4
print(2 ** 3 ** 2)           # Output: 512
# GOTCHA: -2 ** 2 is -(2 ** 2), so -4 and not 4.
# GOTCHA: ** goes right to left, so 2 ** 3 ** 2 is 2 ** (3 ** 2).

# 10. Membership: in / not in
print("a" in "cat")          # Output: True
print(3 not in [1, 2])       # Output: True

# 11. Bitwise operators work on the binary form: & | ^ << >>
print(5 & 3)                 # Output: 1
print(5 | 3)                 # Output: 7
print(5 ^ 3)                 # Output: 6
print(5 << 1)                # Output: 10
print(bin(5))                # Output: 0b101
# KEY: 5 is 101 and 3 is 011 in binary. & keeps shared bits, | keeps any, ^ keeps different ones.

# 12. + and * also work on strings and lists
print("ab" * 3)              # Output: ababab
print([1] + [2])             # Output: [1, 2]
# GOTCHA: "5" + 5 is a TypeError. Python won't mix str and int for you. Use str(5) or int("5").

