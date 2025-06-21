#/usr/bin/python3

# Create an empty set to store colors
color_set = set()

# Prompt the user to enter 5 colors
print("Enter 5 colors:")
for i in range(5):
    color = input(f"Color {i+1}: ").strip().lower()  # Normalize input
    color_set.add(color)

# Display the set of unique colors
print("\nUnique colors you entered:")
print(color_set)

# Try adding a duplicate color
duplicate_color = list(color_set)[0]  # Pick one of the already-entered colors
print(f"\nTrying to add duplicate color: '{duplicate_color}'")
color_set.add(duplicate_color)

# Show that the set remains unchanged
print("Set after attempting to add duplicate:")
print(color_set)

# Show how many unique colors were added
print(f"\nNumber of unique colors: {len(color_set)}")
