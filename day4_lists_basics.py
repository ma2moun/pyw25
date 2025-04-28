# Working with lists
# Creating lists
names = ["Ahmed", "Mazen", "Fatima", "Anas", "Muhannad"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Nissan", 3.9, True, [1, 2, 3]]

print("List examples:")
print(f"Names: {names}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Accessing elements
print("\nAccessing elements:")
print(f"First name: {names[0]}")
print(f"Last name: {names[-1]}")
print(f"Nested list element: {mixed[3][1]}")

# Modifying lists
print("\nModifying lists:")
names[1] = "Basem"
print(f"Updated names list: {names}")

# List methods
print("\nList methods:")
# Adding elements
names.append("Osama")
print(f"After append: {names}")

names.insert(2, "Juri")
print(f"After insert: {names}")

more_names = ["Said", "Arwa"]
names.extend(more_names)
print(f"After extend: {names}")

# Removing elements
removed_name = names.pop(1)
print(f"Removed {removed_name}. Updated list: {names}")

names.remove("Anas")
print(f"After remove 'Anas': {names}")

# Other operations
print("\nOther list operations:")
print(f"Number of names: {len(names)}")
print(f"'Juri' is at index: {names.index('Juri')}")
print(f"Count of 'Mazen': {names.count('Mazen')}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"Sorted numbers: {numbers}")

names.sort()
print(f"Sorted fruits: {names}")

names.reverse()
print(f"Reversed names: {names}")

# Slicing
print("\nList slicing:")
print(f"First three names: {names[:3]}")
print(f"Last three names: {names[-3:]}")
print(f"Middle names: {names[2:5]}")
