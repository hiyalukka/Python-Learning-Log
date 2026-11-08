# Part 2 of the data types log: set, frozenset, range, bytes, bytearray, memoryview
# (Part 1 covers int, float, str, bool, None, complex and type conversion.)

# 1. set: unordered, unique items only
s = {1, 2, 2, 3, 3, 3}
print(s)                     # Output: {1, 2, 3}
print(type(s))               # Output: <class 'set'>
# KEY: duplicates are dropped automatically, and there is no indexing (s[0] fails).
print(type({}))              # Output: <class 'dict'>
print(type(set()))           # Output: <class 'set'>
# GOTCHA: {} is an empty DICT, not an empty set. Use set() for an empty set.

# 2. Set operations (the math kind)
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b)                 # Output: {1, 2, 3, 4, 5}   (union)
print(a & b)                 # Output: {3, 4}            (intersection)
print(a - b)                 # Output: {1, 2}            (in a, not in b)
print(a ^ b)                 # Output: {1, 2, 5}         (in one, not both)
print({1, 2} <= a)           # Output: True              (subset check)
# KEY: set order is not guaranteed. Use sorted(s) when you need a stable order.

# 3. Adding and removing: remove() vs discard()
s = {1, 2, 3}
s.add(4)
s.add(2)                     # already there, so nothing changes
print(s)                     # Output: {1, 2, 3, 4}
s.discard(10)                # missing item: silently does nothing
try:
    s.remove(10)             # missing item: raises an error
except KeyError as e:
    print(type(e).__name__)  # Output: KeyError
# GOTCHA: remove() crashes on a missing item, discard() does not.

# 4. Set items must be hashable (immutable)
print({(1, 2)})              # Output: {(1, 2)}
try:
    {[1, 2]}
except TypeError as e:
    print(e)                 # Output: unhashable type: 'list'
# WHY: sets find items by hash, so an item that can change cannot be stored.
# KEY: tuples, strings, numbers are fine. Lists, dicts, sets are not.

# 5. Most common use: remove duplicates and fast membership checks
nums = [3, 1, 3, 2, 1]
print(sorted(set(nums)))                 # Output: [1, 2, 3]
print(list(dict.fromkeys(nums)))         # Output: [3, 1, 2]
print(3 in {1, 2, 3})                    # Output: True
# KEY: set(nums) loses the original order. dict.fromkeys() keeps first-seen order.
# WHY: `x in set` is fast (near instant), while `x in list` scans every item.

# 6. frozenset: an immutable set
fs = frozenset([1, 2, 3])
print(fs)                    # Output: frozenset({1, 2, 3})
try:
    fs.add(4)
except AttributeError as e:
    print(e)                 # Output: 'frozenset' object has no attribute 'add'
print(fs | {3, 4})           # Output: frozenset({1, 2, 3, 4})
# KEY: set operations still work and return a new frozenset.
d = {frozenset([1, 2]): "pair"}
print(d[frozenset([2, 1])])  # Output: pair
# WHY: because it is hashable, a frozenset can be a dict key or live inside a set.
# Order does not matter, so frozenset([1, 2]) equals frozenset([2, 1]).

# 7. range: a lazy sequence of integers
r = range(5)
print(r)                     # Output: range(0, 5)
print(list(r))               # Output: [0, 1, 2, 3, 4]
print(list(range(2, 10, 2))) # Output: [2, 4, 6, 8]
print(list(range(5, 0, -1))) # Output: [5, 4, 3, 2, 1]
# KEY: range(start, stop, step). The stop value is NOT included.
# GOTCHA: print(range(5)) shows range(0, 5), not the numbers. Wrap it in list().

# 8. range does not store its numbers, so it is tiny even when huge
print(len(range(10 ** 12)))  # Output: 1000000000000
print(500 in range(1000))    # Output: True
print(range(10)[3])          # Output: 3
print(range(10)[-1])         # Output: 9
# WHY: range only stores start, stop and step, then calculates each value on demand.
try:
    range(0.5)
except TypeError as e:
    print(e)                 # Output: 'float' object cannot be interpreted as an integer
# GOTCHA: range only accepts integers, never floats.

# 9. bytes: an immutable sequence of numbers from 0 to 255
b = b"hello"
print(b)                     # Output: b'hello'
print(type(b))               # Output: <class 'bytes'>
print(b[0])                  # Output: 104
print(list(b))               # Output: [104, 101, 108, 108, 111]
try:
    b[0] = 72
except TypeError as e:
    print(type(e).__name__)  # Output: TypeError
# GOTCHA: indexing bytes gives an int (104), not a character. "hello"[0] gives 'h'.

# 10. encode() and decode(): str <-> bytes
text = "héllo"
data = text.encode("utf-8")
print(data)                  # Output: b'h\xc3\xa9llo'
print(len(text), len(data))  # Output: 5 6
print(data.decode("utf-8"))  # Output: héllo
print(bytes([72, 105]))      # Output: b'Hi'
print(bytes(3))              # Output: b'\x00\x00\x00'
# KEY: str is text, bytes is raw data. Files, networks and APIs deal in bytes.
# WHY: "é" takes 2 bytes in UTF-8, so the byte length can be larger than the text length.
# GOTCHA: bytes(3) makes 3 zero bytes. It does NOT convert the number 3.

# 11. bytearray: the mutable version of bytes
ba = bytearray(b"hello")
ba[0] = 72
print(ba)                    # Output: bytearray(b'Hello')
ba.append(33)
print(ba)                    # Output: bytearray(b'Hello!')
print(bytes(ba))             # Output: b'Hello!'
try:
    ba.append(300)
except ValueError as e:
    print(e)                 # Output: byte must be in range(0, 256)
# KEY: bytes is to bytearray what tuple is to list (immutable vs mutable).
# GOTCHA: every value must stay between 0 and 255.

# 12. memoryview: look at the same bytes without copying them
data = bytearray(b"abcdef")
mv = memoryview(data)
print(mv[0])                 # Output: 97
mv[0] = 65
print(data)                  # Output: bytearray(b'Abcdef')
part = mv[1:3]
print(bytes(part))           # Output: b'bc'
part[0] = 66
print(data)                  # Output: bytearray(b'ABcdef')
print(mv.nbytes)             # Output: 6
# KEY: a memoryview slice is a window onto the SAME memory, not a copy.
# WHY: slicing a bytearray copies the data. A memoryview slice does not, which saves
# memory and time on large buffers.
ro = memoryview(b"abc")
print(ro.readonly)           # Output: True
try:
    ro[0] = 1
except TypeError as e:
    print(e)                 # Output: cannot modify read-only memory
# GOTCHA: a memoryview over bytes is read-only. Over a bytearray it is writable.

# 13. Quick summary: mutable or not?
# set        -> mutable,   unique items, unordered
# frozenset  -> immutable, hashable (usable as dict key)
# range      -> immutable, lazy integers
# bytes      -> immutable, numbers 0-255
# bytearray  -> mutable,   numbers 0-255
# memoryview -> a window onto another object's bytes (no copy)
