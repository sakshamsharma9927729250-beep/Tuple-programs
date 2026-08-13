# ============================================
# PROGRAM 1: Creating and Accessing Dictionary
# ============================================

print("=" * 50)
print("PROGRAM 1: Creating and Accessing Dictionary")
print("=" * 50)

# Create a dictionary with student information
student = {
    "name": "Rajesh",
    "age": 20,
    "roll_no": 101,
    "cgpa": 8.5
}

# Print the entire dictionary
print("Student Dictionary:", student)

# Access individual elements using keys
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Roll No: {student['roll_no']}")
print(f"CGPA: {student['cgpa']}")

# Using get() method (safer method to access)
print(f"City: {student.get('city', 'Not found')}")
print("\n")


# ============================================
# PROGRAM 2: Adding and Updating Dictionary
# ============================================

print("=" * 50)
print("PROGRAM 2: Adding and Updating Dictionary")
print("=" * 50)

# Create a dictionary
person = {
    "name": "Priya",
    "age": 22
}

print("Original Dictionary:", person)

# Add new key-value pairs
person["city"] = "Delhi"
person["occupation"] = "Engineer"
print("After adding new items:", person)

# Update existing values
person["age"] = 23
person["name"] = "Priya Sharma"
print("After updating items:", person)

# Using update() method to add multiple items at once
person.update({"phone": "9876543210", "email": "priya@gmail.com"})
print("After using update():", person)
print("\n")


# ============================================
# PROGRAM 3: Deleting Items from Dictionary
# ============================================

print("=" * 50)
print("PROGRAM 3: Deleting Items from Dictionary")
print("=" * 50)

# Create a dictionary with fruits and their prices
fruits = {
    "apple": 50,
    "banana": 30,
    "mango": 80,
    "orange": 40,
    "grapes": 100
}

print("Original Dictionary:", fruits)

# Delete a specific item using del
del fruits["banana"]
print("After deleting 'banana':", fruits)

# Remove and return an item using pop()
price = fruits.pop("orange")
print(f"Removed 'orange' with price: {price}")
print("After using pop():", fruits)

# Remove last inserted item using popitem()
last_item = fruits.popitem()
print(f"Removed last item: {last_item}")
print("After using popitem():", fruits)

# Clear all items from dictionary
fruits_copy = {"apple": 50, "banana": 30}
fruits_copy.clear()
print("After clearing dictionary:", fruits_copy)
print("\n")


# ============================================
# PROGRAM 4: Iterating Through Dictionary
# ============================================

print("=" * 50)
print("PROGRAM 4: Iterating Through Dictionary")
print("=" * 50)

# Create a dictionary with marks of students
marks = {
    "Raj": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88,
    "Vikram": 95
}

# Iterate through keys only
print("All Students (Keys):")
for key in marks:
    print(f"  - {key}")

# Iterate through values only
print("\nAll Marks (Values):")
for value in marks.values():
    print(f"  - {value}")

# Iterate through both keys and values
print("\nStudents and their Marks (Key-Value Pairs):")
for key, value in marks.items():
    print(f"  {key}: {value}")

# Using enumerate() with dictionary items
print("\nWith Index:")
for index, (student, mark) in enumerate(marks.items(), 1):
    print(f"  {index}. {student} - {mark}")
print("\n")


# ============================================
# PROGRAM 5: Dictionary Methods and Operations
# ============================================

print("=" * 50)
print("PROGRAM 5: Dictionary Methods and Operations")
print("=" * 50)

# Create two dictionaries
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "c": 4,
    "d": 5,
    "e": 6
}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# Check if key exists
print(f"\nIs 'a' in dict1? {'a' in dict1}")
print(f"Is 'x' in dict1? {'x' in dict1}")

# Get all keys, values, and items
print(f"\nKeys in dict1: {list(dict1.keys())}")
print(f"Values in dict1: {list(dict1.values())}")
print(f"Items in dict1: {list(dict1.items())}")

# Get the size of dictionary
print(f"\nNumber of items in dict1: {len(dict1)}")

# Copy a dictionary
dict3 = dict1.copy()
print(f"\nCopied dictionary: {dict3}")

# Create dictionary from list of tuples
list_items = [("x", 10), ("y", 20), ("z", 30)]
dict4 = dict(list_items)
print(f"Dictionary from list of tuples: {dict4}")

# Merge two dictionaries (Python 3.9+)
dict5 = {**dict1, **dict2}
print(f"\nMerged dictionary (dict1 + dict2): {dict5}")

# Sort dictionary by keys
sorted_dict = dict(sorted(dict5.items()))
print(f"Dictionary sorted by keys: {sorted_dict}")

# Sort dictionary by values
sorted_by_value = dict(sorted(dict5.items(), key=lambda x: x[1]))
print(f"Dictionary sorted by values: {sorted_by_value}")

print("\n" + "=" * 50)
print("All 5 Programs Completed Successfully!")
print("=" * 50)
