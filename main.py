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
