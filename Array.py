names = ["Jennifer", "Mary", "Yohance"]  # Create a list of names

names[0] = "Jedidiah"  # Change Jennifer to Jedidiah
print(names)  # Print the updated list

for element in names:  # Loop through each name in the list
    print(element)  # Print each name one by one

names.append("BSIS")  # Add BSIS to the end of the list
print(names)  # Print the updated list

names.insert(1, "Gwen")  # Insert Gwen at index 1
print(names)  # Print the updated list

names.pop()  # Remove the last element from the list
print(names)  # Print the updated list

names.remove("Gwen")  # Remove Gwen from the list
print(names)  # Print the updated list

if "Jennifer" in names:  # Check if Jennifer is in the list
    print("found!")  # Print found if Jennifer exists
else:  # Execute if Jennifer is not in the list
    print("not found")  # Print not found