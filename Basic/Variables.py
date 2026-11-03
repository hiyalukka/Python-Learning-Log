# 1. A variable is a name that points to a value; = binds the name to it
score = 90
print(score)                 # Output: 90
# WHY: Python has no "boxes that hold values", only names pointing at objects.

# 2. Reassigning just re-points the name (the type can change too)
score = "ninety"
print(score)                 # Output: ninety

# 3. Multiple assignment: several names in one line
a, b, c = 1, 2, 3
print(a, b, c)               # Output: 1 2 3
x = y = 0                    # both names point to the same 0
print(x, y)                  # Output: 0 0

# 4. Left and right side must match in count when unpacking
try:
    p, q = 1, 2, 3
except ValueError as e:
    print(e)                 # Output: too many values to unpack (expected 2)
# GOTCHA: this is a runtime ValueError, not a SyntaxError. Python only counts when it runs.

# 5. Swap two variables without a temp
m, n = 1, 2
m, n = n, m
print(m, n)                  # Output: 2 1
# WHY: the right side is fully evaluated first as (2, 1), then unpacked into m and n.

# 6. Star unpacking: * collects the leftovers into a list
first, *rest = [10, 20, 30, 40]
print(first, rest)           # Output: 10 [20, 30, 40]

# 7. Two names, one object (mutable types like list)
nums = [1, 2, 3]
alias = nums                 # NOT a copy, same list with two names
alias.append(4)
print(nums)                  # Output: [1, 2, 3, 4]
print(nums is alias)         # Output: True
# GOTCHA: `alias = nums` does not copy. Use nums.copy() for a real copy.
independent = nums.copy()
independent.append(5)
print(nums)                  # Output: [1, 2, 3, 4]

# 8. Immutable types (int, str, tuple) can't change in place
n1 = 5
n2 = n1
n2 += 1
print(n1, n2)                # Output: 5 6
# WHY: n2 += 1 builds a new int and re-points n2. n1 never moves.

# 9. Naming rules: letters, digits, underscore; can't start with a digit; no keywords
import keyword
print("my_var".isidentifier())     # Output: True
print("2var".isidentifier())       # Output: False
print("my-var".isidentifier())     # Output: False
print(keyword.iskeyword("class"))  # Output: True
# KEY: snake_case for variables (PEP 8). Names are case-sensitive.

# 10. UPPER_CASE is a constant by convention only, Python won't stop you
MAX_RETRIES = 3
MAX_RETRIES = 5
print(MAX_RETRIES)           # Output: 5
# GOTCHA: there are no real constants in Python. The capital letters are a promise, not a lock.

# 11. del removes the name, not the value
temp = 42
del temp
try:
    print(temp)
except NameError as e:
    print(e)                 # Output: name 'temp' is not defined
