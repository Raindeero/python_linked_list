class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        """Prints linked list from the head to tail, while the Node is not None"""
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

    def add_to_start(self, data):
        """Insert a new element at the beginning of the linked list"""
        new_element = Node(data)
        new_element.next = self.head
        self.head = new_element

    def add_to_end(self, data):
        """Insert a new element at the end of the linked list"""
        new_element = Node(data)
        # Checking that the list is not empty
        if self.head is None:
            self.head = new_element
            return
        last_element = self.head
        # Find the last element of the linked list. While last_element.next is not None cycle will continue
        while last_element.next:
            last_element = last_element.next
        # Add a new element at the next
        last_element.next = new_element

    def add_element_after(self, after, data):
        new_element = Node(data)
        if self.head is None:
            print("List is empty!")
            return
        prev = self.head
        while prev:
            if prev.data == after:
                new_element.next = prev.next
                prev.next = new_element
                return
            prev = prev.next

    def del_element_by_data(self, data):
        """Remove the element of the list by data"""
        element = self.head
        if element is None:
            print("List is empty")
            return
        # if the element at the beginning
        if element.data == data:
            self.head = element.next
            element = None
            return
        # search the item with data. Going through the list while element is not None and the element.data is not
        # equal that we are searching for.
        while element:
            if element.data == data:
                break
            prev = element
            element = element.next
        prev.next = element.next
        element = None

    def del_list(self):
        """Deleting whole linked list"""
        if self.head is None:
            print("List is empty")
            return
        # While head is not empty
        while self.head:
            to_delete = self.head
            self.head = self.head.next
            to_delete = None
        print("List was deleted")


llist = LinkedList()
llist.head = Node("Monday")
second_element = Node("Tuesday")
third_element = Node("Wednesday")

llist.head.next = second_element
second_element.next = third_element

llist.add_to_start("Thursday")
llist.add_to_end("Friday")
# llist.list_print()
llist.del_element_by_data("Thursday")
llist.del_element_by_data("Friday")
llist.list_print()
llist.add_element_after("Tuesday", "Friday")
llist.list_print()
# llist.del_list()
# llist.list_print()
