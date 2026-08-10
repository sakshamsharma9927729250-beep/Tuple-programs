# Program 1: Basic tuple creation and operations
# A tuple is an immutable ordered collection in Python.
# Once created, tuple elements cannot be changed in place.

def basic_tuple_demo():
    # Create a tuple with different data types
    colors = ("red", "green", "blue")
    print("Tuple:", colors)

    # Access elements by index
    print("First color:", colors[0])
    print("Last color:", colors[-1])

    # Slicing returns a new tuple
    print("First two colors:", colors[0:2])

    # Tuple length
    print("Number of colors:", len(colors))

    # Tuples can be nested
    nested = (1, (2, 3), 4)
    print("Nested tuple:", nested)


# Program 2: Tuple unpacking and using tuple functions
# Tuple unpacking assigns elements to variables in one step.
# Common tuple functions include count() and index().

def tuple_unpacking_demo():
    # Define a tuple of student scores
    scores = (95, 82, 78, 95, 88)
    print("Scores:", scores)

    # Unpack into variables
    first_score, second_score, third_score, fourth_score, fifth_score = scores
    print("First score:", first_score)
    print("Second score:", second_score)

    # Count occurrences of a value in the tuple
    duplicate_count = scores.count(95)
    print("Number of times 95 appears:", duplicate_count)

    # Find the index of a value
    position = scores.index(88)
    print("Index of 88:", position)


# Program 3: Tuple immutability and tuple methods
# Tuples are immutable, so they cannot be changed after creation.

def tuple_immutability_demo():
    numbers = (10, 20, 30, 20)
    print("Numbers:", numbers)

    print("Count of 20:", numbers.count(20))
    print("Index of 30:", numbers.index(30))

    try:
        numbers[0] = 99
    except TypeError as error:
        print("Tuple is immutable:", error)


# Program 4: Converting between tuple and list
# You can convert tuples to lists and back again.

def tuple_conversion_demo():
    days = ("Mon", "Tue", "Wed")
    print("Original tuple:", days)

    day_list = list(days)
    day_list.append("Thu")
    print("List after adding an item:", day_list)

    updated_tuple = tuple(day_list)
    print("Tuple after converting back:", updated_tuple)


if __name__ == "__main__":
    print("=== Tuple Basic Demo ===")
    basic_tuple_demo()
    print()
    print("=== Tuple Unpacking Demo ===")
    tuple_unpacking_demo()
    print()
    print("=== Tuple Immutability Demo ===")
    tuple_immutability_demo()
    print()
    print("=== Tuple Conversion Demo ===")
    tuple_conversion_demo()
