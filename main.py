from linked_list import LinkedList

# llist = LinkedList()
# llist.head = Node("Monday")
# second_element = Node("Tuesday")
# third_element = Node("Wednesday")

# llist.head.next = second_element
# second_element.next = third_element

# llist.add_to_start("Thursday")
# llist.add_to_end("Friday")
# llist.list_print()
# llist.del_element_by_data("Thursday")
# llist.del_element_by_data("Friday")
# llist.list_print()
# llist.add_element_after("Tuesday", "Friday")
# llist.list_print()
# llist.del_list()
# llist.list_print()

linked_list = LinkedList()
linked_list.add_to_end(1)
linked_list.add_to_end(2)
linked_list.add_to_end(3)

# Сохранение списка в файл
linked_list.save_list_to_file("linked_list.txt")

# Создание нового списка и загрузка из файла
loaded_list = LinkedList()
loaded_list = loaded_list.load_list_from_file("linked_list.txt")

# Вывод списка после загрузки
loaded_list.list_print()
