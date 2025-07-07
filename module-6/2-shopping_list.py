#/usr/bin/python3

# Create a list with at least 5 grocery items
grocery_list = ["milk", "bread", "eggs", "apples", "rice"]

# Print the entire list
print("Original grocery list:")
print(grocery_list)

# Add a new item to the list
grocery_list.append("cheese")
print("\nAfter adding 'cheese':")
print(grocery_list)

# Remove an item from the list (e.g., "bread")
grocery_list.remove("bread")
print("\nAfter removing 'bread':")
print(grocery_list)

# Display the final list using slicing (showing all items)
print("\nFinal grocery list:")
print(grocery_list[:])
