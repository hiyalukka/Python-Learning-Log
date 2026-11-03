# 1. Syntax = grammar Python needs to read your code; semantics = what the code means
price = 100
discount = 20
final = price + discount   # valid syntax, wrong meaning: I meant to subtract
print(final)
# Output: 120 (Python can't catch semantic mistakes, only testing can)

# 2. Python is case-sensitive: name and Name are different variables
name = "Kartik"
Name = "Keshvi"
print(name)
# Output: Kartik
print(Name)
# Output: Keshvi

# 3. Indentation (4 spaces) groups code into blocks; a colon opens the block
age = 32
if age > 30:
    print("inside the if block")
# Output: inside the if block
print("outside the block")
# Output: outside the block

# 4. Indentation mistakes raise IndentationError (a kind of SyntaxError) before anything runs
broken = {
    "missing indent": "if True:\nprint('hi')",
    "missing colon": "if True\n    print('hi')",
}
for label, code in broken.items():
    try:
        compile(code, "<example>", "exec")
    except SyntaxError as e:
        print(label, "->", type(e).__name__)
# Output: missing indent -> IndentationError
# Output: missing colon -> SyntaxError

# 5. NameError happens while running, not before (unlike SyntaxError)
try:
    result = undefined_variable
except NameError as e:
    print(e)
# Output: name 'undefined_variable' is not defined

# 6. Comments: # for single lines; Python has no real multi-line comment
# (a triple-quoted string works but is really meant for docstrings)

# 7. Continue a long line with brackets (preferred) or a backslash
total = (1 + 2 + 3 +
         4 + 5 + 6)
print(total)
# Output: 21

# 8. Python infers the type from the value, and a variable can be re-pointed
variable = 10
print(type(variable))
# Output: <class 'int'>
variable = "Kritika"
print(type(variable))
# Output: <class 'str'>
