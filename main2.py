# Program 5: Tuple membership and comparison
# You can check whether an item exists in a tuple using 'in' or 'not in'.
# Tuples can also be compared lexicographically, item by item.

def tuple_membership_and_comparison_demo():
    # Create a tuple of fruits
    fruits = ("apple", "banana", "cherry")
    print("Fruits tuple:", fruits)

    # Check membership in the tuple
    print("Is 'banana' present?", "banana" in fruits)
    print("Is 'mango' present?", "mango" not in fruits)

    # Compare two tuples
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 4)
    print("Tuple1 < Tuple2:", tuple1 < tuple2)


# Program 6: Tuple repetition and concatenation
# Repeating a tuple creates multiple copies of its elements.
# Concatenation joins two tuples into one larger tuple.

def tuple_repetition_and_concat_demo():
    # Create a base tuple
    base = ("Python", "Java")

    # Repeat the tuple twice
    repeated = base * 2
    print("Repeated tuple:", repeated)

    # Add another tuple using concatenation
    extra = ("C++", "JavaScript")
    combined = base + extra
    print("Combined tuple:", combined)

    # Loop through the combined tuple
    print("Languages:")
    for language in combined:
        print("-", language)


if __name__ == "__main__":
    print("=== Tuple Membership and Comparison Demo ===")
    tuple_membership_and_comparison_demo()
    print()
    print("=== Tuple Repetition and Concatenation Demo ===")
    tuple_repetition_and_concat_demo()
