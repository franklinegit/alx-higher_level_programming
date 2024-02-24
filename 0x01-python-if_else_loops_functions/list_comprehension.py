bits = [True, False, False, True, False, True, True]
str = "HelloMyNameIsOdd"

newbits = []
for b in bits:
    if b == True:
        newbits.append(1)
    else:
        newbits.append(0)
print("newbits made by append(): {}".format(newbits))

superbits = [1 if b == True else 0 for b in bits]
print (f"superbits made by list comprehension: {superbits}")

lst_str = [i for i in str]
print("list of characters", lst_str)

join_str = "".join([i for i in str])
print("joined string:", join_str)

space_str = "".join([i if i.islower() else " " + i.lower() if i in ["N", "I"] else " " + i for i in str])[1:]
print("spaced string:", space_str)