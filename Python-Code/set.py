Unordered, mutable, unique collection.

Syntax: {} or set().

No duplicate elements.

Elements must be hashable (int, str, tuple, etc.).

🔹 Create Set
s = {1, 2, 3}               # literal
s = set([1, 2, 2, 3])       # from iterable → {1, 2, 3}
s = set()                   # empty set ({} = dict!)

🔹 Add & Remove
s.add(4)           # add single element
s.update([5, 6])   # add multiple elements
s.remove(2)        # KeyError if not found
s.discard(10)      # safe remove (no error)
s.pop()            # remove random element
s.clear()          # empty the set

🔹 Access

Sets are unordered → no indexing/slicing.

Iterate instead:

for val in s:
    print(val)

🔹 Set Operations (Math-like)
A = {1, 2, 3}
B = {3, 4, 5}

A | B     # union → {1, 2, 3, 4, 5}
A & B     # intersection → {3}
A - B     # difference → {1, 2}
A ^ B     # symmetric diff → {1, 2, 4, 5}

🔹 Membership Test
if 2 in A: ...
if 10 not in A: ...


👉 O(1) average time complexity.

🔹 Frozen Set

Immutable version of set:

fs = frozenset([1, 2, 3])


Can be used as dict keys or inside other sets.

🔹 Useful Methods
len(s)                 # size
min(s), max(s)         # min/max element
s.issubset(B)          # A ⊆ B
s.issuperset(B)        # A ⊇ B
s.isdisjoint(B)        # no common elements