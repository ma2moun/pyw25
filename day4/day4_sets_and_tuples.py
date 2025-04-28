"""
### NOTES:
## Sets:
sets don't accept duplicates
sets don't save location of items
sets accept change

## Tuples:
tuples don't accept change
tuples save location of items
tuples accept duplications
"""

numbers={3,2,4,1,9,12,9}

print(f"Numbers: {numbers}")

# Add a number
numbers.add(24)
print(f"Number 24 was added. Updated Numbers: {numbers}")

# Remove a number
numbers.remove(2)
print(f"Number 2 was removed. Updated Numbers: {numbers}")

# Pop method
removed_number=numbers.pop()
print(f"{removed_number} was removed. Updated Numbers: {numbers}")


# Another set
numbers2={3,2,99,1,4}

# Intersection
intersect=numbers.intersection(numbers2)
print(f"The sets intersect in {intersect}")

# Union
Union=numbers.union(numbers2)
print(f"The sets union in {Union}")

# =======================================================

# TUPLES

coordinates=(22.32, 44.22)
print(coordinates)

# Check count of 22.32
print(f"count of 22.32 is {coordinates.count(22.32)}")

# Check index of 44.22
print(f"Index of 44.22 is {coordinates.index(44.22)}")


# However, to edit a tuple: change it to set or list:
# To list
clist= list(coordinates)
print(f"Type of clist now is: {type(clist)}")

# add a value to clist:
clist.append(100.100)

# Change back to a tuple
coordinates=tuple(clist)
print(f"The tuple after update is {coordinates}")

# Similarily can be changed to a set
cset=set(coordinates)
print(f"The tuple after changing to a set {cset}")

