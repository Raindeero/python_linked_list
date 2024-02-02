# Singly Linked List in Python

This project represents an implementation of a singly linked list in the Python programming language. 
It includes basic operations for working with a singly linked list.

## Project Structure

- `linked_list.py`: The main module containing definitions for the `Node` and `LinkedList` classes, as well as the implementation of basic operations on a singly linked list.
- `main.py`: An example showcasing the usage of basic functions.
- `README.md`: This file, providing an overview of the project and instructions.

## How to Use

1. Install Python (if not already installed).
2. Run `main.py` for a usage example and a demonstration of functionality.

```bash
from linked_list import LinkedList

# Create a linked list
linked_list = LinkedList()

# Add elements to the list
linked_list.add_to_end(1)
linked_list.add_to_end(2)
linked_list.add_to_end(3)

# Print the original list
print("Original List:")
linked_list.list_print()

# Add an element to the start
linked_list.add_to_start(0)

# Add an element after a specific value
linked_list.add_element_after(2, 2.5)

# Print the modified list
print("\nModified List:")
linked_list.list_print()

# Delete an element by data
linked_list.del_element_by_data(1)

# Print the list after deletion
print("\nList after Deletion:")
linked_list.list_print()

# Save the list to a file
linked_list.save_list_to_file("linked_list.txt")

# Load the list from a file
loaded_list = LinkedList()
loaded_list = loaded_list.load_list_from_file("linked_list.txt")

# Print the loaded list
print("\nLoaded List:")
loaded_list.list_print()

