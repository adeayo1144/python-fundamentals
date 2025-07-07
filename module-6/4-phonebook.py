#/usr/bin/python3

# Create a phonebook dictionary with at least 3 contacts
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-666-7777"
}

# Print all keys and values
print("Phonebook entries:")
for name, number in phonebook.items():
    print(f"{name}: {number}")

# Update a contact's number (e.g., Bob's number)
phonebook["Bob"] = "111-222-3333"
print("\nAfter updating Bob's number:")
for name, number in phonebook.items():
    print(f"{name}: {number}")

# Delete a contact (e.g., Charlie)
del phonebook["Charlie"]
print("\nAfter deleting Charlie:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
