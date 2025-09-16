tuple = ("yellow","pink","red","purple","blue")
print(tuple)

# -------------------------
if "brown" in tuple:
    print("blue is there")
else:
    print("value is not there")

# --------------------------
# print(tuple.count("purple"))

# --------------------------
# Slicing
print(tuple[-1])
print(tuple[2:4])


# --------------------------
# TUPLE TO LIST - so we can modify list as tuple is immutable
lst = list(tuple)
print(lst)