# ============================================
# Program 1: Reading a File Line by Line
# ============================================
# This program demonstrates how to read a file
# and process its contents line by line.

def read_file_line_by_line(filename):
    """
    Function to read and display file contents line by line.
    Args: filename (str) - Name of the file to read
    """
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            line_number = 1
            # Read each line from the file
            for line in file:
                # strip() removes newline characters
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error occurred: {e}")


# ============================================
# Program 2: Writing Data to a File
# ============================================
# This program demonstrates how to write data
# to a file and append new content.

def write_to_file(filename, data):
    """
    Function to write data to a file.
    Args: 
        filename (str) - Name of the file to write to
        data (list) - List of strings to write
    """
    try:
        # Open file in write mode ('w') - creates or overwrites
        with open(filename, 'w') as file:
            file.write("=" * 50 + "\n")
            file.write("Data Written to File\n")
            file.write("=" * 50 + "\n\n")
            
            # Write each data item to the file
            for item in data:
                file.write(f"- {item}\n")
        
        print(f"Data successfully written to '{filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")


def append_to_file(filename, new_data):
    """
    Function to append data to an existing file.
    Args: 
        filename (str) - Name of the file to append to
        new_data (str) - Data to append
    """
    try:
        # Open file in append mode ('a') - adds to existing content
        with open(filename, 'a') as file:
            file.write(f"\n{new_data}\n")
        print(f"Data successfully appended to '{filename}'")
    except Exception as e:
        print(f"Error appending to file: {e}")


# ============================================
# Main Program - Testing the Functions
# ============================================
if __name__ == "__main__":
    # Test data
    student_data = [
        "Alice - Scored 92 in Mathematics",
        "Bob - Scored 85 in Physics",
        "Charlie - Scored 88 in Chemistry"
    ]
    
    # Test Program 1: Writing to file
    write_to_file("student_records.txt", student_data)
    
    # Test Program 2: Appending to file
    append_to_file("student_records.txt", "New Entry: Diana - Scored 95 in Biology")
    
    # Read and display the file
    print("\n" + "="*50)
    print("Reading the file:")
    print("="*50 + "\n")
    read_file_line_by_line("student_records.txt")