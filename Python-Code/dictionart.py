dict = {"one": "yellow",
        "two":"pink",
        "three":"red",
        "four":"purple",
        "five":"blue"
        }

# Accessing dict
print(dict.get("two"))  #if key doesn't exist, code doesn't Raise an error
print(dict["two"])      #if key doesn't exist, code Raise an error
        # ------Use case------
        # .get(key) = Safe lookups (when not sure if key exists)
        # dict[key] = Strict lookups (when you expect the key must be there)
# --------------------------------------------------

# Length of dict
print(len(dict))

# for key, value in dict.items():
#     print(key, value)

# Adding item in dict
dict["six"] = "maroon"

# print(dict["six"])

# print(dict.items())

# --------------------------------
# Getting Dictionary Values as a List
values = dict.values()
print(values)
# Getting Dictionary Keys as a List
keys = dict.keys()
print(keys)


# ---------------------------
# LOOPING
for k in dict:
    print(k)
for v in dict.values():
    print(v)
for k,v in dict.items():
    print(k,v)
