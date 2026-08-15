# Set Programs in Python
# A set is an unordered collection of unique items.
# It does not allow duplicate values and supports mathematical set operations.

# Program 1: Create a set and print it
# This program shows how to create a set and how duplicates are removed automatically.
def program_1_basic_set():
    # A set of fruits; duplicate values are ignored automatically.
    fruits = {"apple", "banana", "mango", "apple", "orange"}

    print("Program 1: Basic Set")
    print("Fruits set:", fruits)
    print("Total items:", len(fruits))
    print()


# Program 2: Add, remove and update items in a set
# We can insert new values and delete existing ones using add() and remove().
def program_2_set_operations():
    # Create an empty set
    numbers = set()

    # Add items to the set
    numbers.add(10)
    numbers.add(20)
    numbers.add(30)
    numbers.add(20)  # Duplicate value is ignored

    print("Program 2: Add/Remove in Set")
    print("Initial set:", numbers)

    # Remove an item
    numbers.remove(20)
    print("After removing 20:", numbers)

    # Add another item
    numbers.add(40)
    print("After adding 40:", numbers)
    print()


# Program 3: Union, intersection and difference
# These are common set operations used in Python.
def program_3_set_math():
    set_a = {1, 2, 3, 4, 5}
    set_b = {3, 4, 5, 6, 7}

    print("Program 3: Set Mathematics")
    print("Set A:", set_a)
    print("Set B:", set_b)

    # Union: all unique items from both sets
    print("Union:", set_a | set_b)

    # Intersection: common items
    print("Intersection:", set_a & set_b)

    # Difference: items present in A but not in B
    print("Difference A-B:", set_a - set_b)

    # Symmetric difference: items that are in one set but not both
    print("Symmetric Difference:", set_a ^ set_b)
    print()


# Program 4: Check membership and iterate through a set
# We can use 'in' to check whether an item exists in a set.
def program_4_membership_loop():
    students = {"Rahul", "Anita", "Sonia", "Karan"}

    print("Program 4: Membership and Loop")
    print("Is Rahul present?", "Rahul" in students)
    print("Is Mohan present?", "Mohan" in students)

    # Iterate over set items
    print("Students:")
    for student in students:
        print("-", student)
    print()


# Program 5: Remove duplicates from a list using a set
# This is a useful real-world example of converting a list to a set.
def program_5_remove_duplicates():
    # Original list with duplicate values
    marks = [90, 85, 90, 95, 85, 100, 95]

    print("Program 5: Remove Duplicates")
    print("Original marks:", marks)

    # Convert list to set to remove duplicates
    unique_marks = set(marks)
    print("Unique marks:", unique_marks)
    print("Sorted unique marks:", sorted(unique_marks))
    print()


# Program 6: Set copy, clear, pop, and discard operations
# These methods help us manage and manipulate sets in different ways.
def program_6_advanced_operations():
    # Original set
    colors = {"red", "blue", "green", "yellow"}

    print("Program 6: Advanced Set Operations")
    print("Original colors set:", colors)

    # Create a copy of the set (important for avoiding reference issues)
    colors_copy = colors.copy()
    print("Copied colors set:", colors_copy)

    # Pop removes and returns an arbitrary item from the set
    removed_item = colors_copy.pop()
    print("Item removed by pop():", removed_item)
    print("After pop():", colors_copy)

    # Discard removes an item without raising error if not found
    colors_copy.discard("blue")
    print("After discard('blue'):", colors_copy)

    # Try to discard an item that doesn't exist (no error)
    colors_copy.discard("purple")
    print("After discard('purple') - no error raised:", colors_copy)

    # Clear empties the entire set
    test_set = {"a", "b", "c"}
    print("Before clear():", test_set)
    test_set.clear()
    print("After clear():", test_set)
    print()


# Program 7: Check subset, superset and find common elements between multiple sets
# This program demonstrates relationships between sets and how to find common elements.
def program_7_set_relationships():
    # Define multiple sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    set3 = {3, 4, 5, 6, 7}

    print("Program 7: Set Relationships and Common Elements")
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Set 3:", set3)

    # Check if set2 is a subset of set1 (all elements of set2 are in set1)
    print("Is Set 2 a subset of Set 1?", set2.issubset(set1))

    # Check if set1 is a superset of set2 (set1 contains all elements of set2)
    print("Is Set 1 a superset of Set 2?", set1.issuperset(set2))

    # Check if two sets are disjoint (have no common elements)
    print("Are Set 1 and Set 3 disjoint?", set1.isdisjoint(set3))

    # Find common elements between multiple sets
    common_elements = set1 & set2 & set3
    print("Common elements in all three sets:", common_elements)

    # Find elements common to set1 and set3
    common_1_3 = set1.intersection(set3)
    print("Common elements between Set 1 and Set 3:", common_1_3)

    # Find all unique elements across all sets
    all_elements = set1 | set2 | set3
    print("All unique elements across sets:", all_elements)
    print()


# Main function to run all programs
# This allows us to execute all 7 examples in one file.
def main():
    program_1_basic_set()
    program_2_set_operations()
    program_3_set_math()
    program_4_membership_loop()
    program_5_remove_duplicates()
    program_6_advanced_operations()
    program_7_set_relationships()


# Run the main function when the file is executed
if __name__ == "__main__":
    main()
