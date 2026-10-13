names = ["Jennifer", "Mary", "Yohance"]

names[0] = "Jedidiah"
print(names)

for element in names:
    print(element)

names.append("BSIS")
print(names)

names.insert(1, "Gwen")
print(names)

names.pop()
print(names)

names.remove("Gwen")
print(names)

if "Jennifer" in names:
    print("found!")
else:
    print("not found")
