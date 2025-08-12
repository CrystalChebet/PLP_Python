# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend the list with another list
my_list.extend([50, 60, 70])
print("The new list is: ", my_list)

# Remove the last element
my_list.pop()
print("The new list after pop is: ",my_list)

# Sort the list in ascending order
my_list.sort()
print("New list after sorting",my_list)

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Print the final list (optional)
print("Final list:", my_list)
