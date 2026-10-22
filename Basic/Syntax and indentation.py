"""
SYNTAX & INDENTATION   |   Topic: Python basics   |   Udemy section: 1.0 Basics
Status:  [x] predicted   [ ] blank-rewrite (next day)   [ ] 7-day review

IN MY OWN WORDS:
    Syntax = the grammar rules Python requires so it can read my code.
    Semantics = what the code actually means / does once it runs.
    Code can be perfect syntax and still do the wrong thing.

I'D REACH FOR THIS WHEN:
    Python throws SyntaxError / IndentationError / NameError and I need to know why.

KEY IDEA:
    Python uses INDENTATION (not braces {}) to group code into blocks.
"""

# =========================================================================
# 1. SYNTAX vs SEMANTICS
# =========================================================================
# Syntax error: Python can't even understand it, so nothing runs.
# Semantic error: Python understands it fine, but it does the wrong thing.
price = 100
discount = 20
final = price + discount     # valid syntax... but I meant to SUBTRACT
print(final)                 # Output: 120
# KEY: Python can't catch semantic mistakes. Only testing and reading do.

#Example: Calculating a student's average marks
#Suppose you scored 80 in Python and 60 in Java. You want to calculate your average.

#Correct code:
python = 80
java = 60

average = (python + java) / 2

print(average)

#Semantic mistake - incorrect logic
python = 80
java = 60

average = (python + java) * 2

print(average)

#Difference between Semantics and Bug
#Semantics = The meaning of your code.
#Bug = A problem in your program that causes it to behave incorrectly or unexpectedly.

# =========================================================================
# 2. CASE SENSITIVITY
# =========================================================================
name = "Kartik"
Name = "Keshvi"
print(name)                  # Output: Kartik
print(Name)                  # Output: Keshvi
# KEY: `name` and `Name` are two different variables.
# GOTCHA: a typo in capitalisation (`Print`, `True` vs `true`) is a NameError, not a warning.

# =========================================================================
# 3. INDENTATION -- how Python groups code into blocks
# =========================================================================
age = 32
if age > 30:
    print("inside the if block")    # Output: inside the if block
print("outside the block")          # Output: outside the block
# KEY: the colon `:` opens a block; the indented lines under it belong to that block.
# KEY: use 4 spaces per level (PEP 8). Never mix tabs and spaces.

# Nested blocks -- each level indents one step further
if True:
    print("level 1")                # Output: level 1
    if False:
        print("never printed")
    print("back at level 1")        # Output: back at level 1
print("level 0")                    # Output: level 0

# =========================================================================
# 4. WHAT BREAKS: syntax errors (triggered safely with compile())
# =========================================================================
broken_examples = {
    "missing indent": "if True:\nprint('hi')",
    "unexpected indent": "x = 1\n    y = 2",
    "inconsistent dedent": "if True:\n        a = 1\n    b = 2",
    "missing colon": "if True\n    print('hi')",
}
for label, code in broken_examples.items():
    try:
        compile(code, "<example>", "exec")
    except SyntaxError as e:
        print(label, "->", type(e).__name__)
# Output:
# missing indent -> IndentationError
# unexpected indent -> IndentationError
# inconsistent dedent -> IndentationError
# missing colon -> SyntaxError
# GOTCHA: IndentationError is a kind of SyntaxError. The program won't start at all.
# GOTCHA: mixing tabs and spaces looks fine on screen but breaks Python. Set your editor to insert spaces.

# NameError -- using a name that was never created (this one is a RUNTIME error)
try:
    result = undefined_variable
except NameError as e:
    print(e)                 # Output: name 'undefined_variable' is not defined
# KEY: SyntaxError = caught BEFORE running. NameError = caught WHILE running.

# =========================================================================
# 5. COMMENTS
# =========================================================================
# This is a single-line comment. Python ignores it.
print("Hello World")         # Output: Hello World

# Python has no real multi-line comment. Two common ways:
# 1) several lines starting with #   (what I'm doing right now)
# 2) a triple-quoted string that isn't assigned to anything:
"""
This works like a block comment,
but it's technically a string Python reads and throws away.
"""
# KEY: use # for comments. Triple quotes are really for docstrings (documentation).

# =========================================================================
# 6. LINE CONTINUATION & MULTIPLE STATEMENTS
# =========================================================================
total = 1 + 2 + 3 + 4 + \
        5 + 6
print(total)                 # Output: 21
# Brackets let you continue a line without a backslash (preferred):
total2 = (1 + 2 + 3 +
          4 + 5 + 6)
print(total2)                # Output: 21
# KEY: inside (), [] or {} you can break lines freely. Prefer that over `\`.
# GOTCHA: a space after the backslash (`\ `) is a SyntaxError.

x = 5; y = 10; z = x + y     # several statements on one line with ;
print(z)                     # Output: 15
# KEY: legal, but rarely good style. One statement per line is easier to read.

# =========================================================================
# 7. TYPE INFERENCE (semantics: Python figures out the type itself)
# =========================================================================
variable = 10
print(type(variable))        # Output: <class 'int'>
variable = "Kritika"
print(type(variable))        # Output: <class 'str'>
# KEY: you never declare a type. The value carries it, and the variable can be re-pointed later.
# GOTCHA: flexible also means a variable can silently change type. Name things clearly.


# Summary:
#   1. Syntax = grammar Python requires (missing colon fails). 
#      Semantics = meaning (adding instead of subtracting runs fine but is wrong).
#   2. Indentation: The space added at the beginning of a line of code to show its structure and which block of code it belongs to.
#   3. Python is case-sensitive. `Print` isn't a built-in, so it raises NameError.
#   4. A backslash `\` or brackets ( ) [ ] { }.
#   5. SyntaxError (found while compiling, before anything runs).
