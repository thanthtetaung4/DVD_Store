"""Linked List Class"""
from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # insert data into linked list
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            if self.head.next is None:
                new_node = Node(data)
                self.head.next = new_node
            else:
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                new_node = Node(data)
                current_node.next = new_node

    # Insert data at index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_size() - 1:
            print("Index out of bound")
            return 0
        else:
            if index == 0:
                new_node = Node(data)
                temp = self.head
                self.head = new_node
                new_node.next = temp
            else:
                prev_node = self.head
                current_node = self.head.next
                current_index = 1
                while current_index <= index:
                    if current_index == index:
                        new_node = Node(data)
                        prev_node.next = new_node
                        new_node.next = current_node
                        return 0
                    else:
                        prev_node = current_node
                        current_node = current_node.next
                        current_index += 1

    # remove data from linked list at input index
    def remove_index(self, index):
        if 0 < index > self.get_size() - 1:
            print("Index out of bound")
            return 0
        else:
            if index == 0:
                print(f"Successfully removed {self.head.data}")
                self.head = self.head.next

            else:
                prev_node = self.head
                current_node = self.head.next
                print(f"first: {current_node.data}")
                current_index = 1
                while current_index <= index:
                    if current_index == index:
                        prev_node.next = current_node.next
                        current_node.next = None
                        print(f"Successfully removed {current_node.data}")
                        return 0
                    else:
                        prev_node = current_node
                        current_node = current_node.next
                        current_index += 1

    def remove_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
        else:
            prev_node = self.head
            current = self.head.next
            while current is not None:
                if current.data == value:
                    prev_node.next = current.next
                    current.next = None
                    return True
                else:
                    prev_node = current
                    current = current.next
            return False


    # get data from linked list at input index
    def get_item_index(self, index):
        if index > self.get_size()-1 or index < 0:
            return None
        else:
            current_node = self.head

            while index > 0 and current_node is not None:
                current_node = current_node.next
                index -= 1
            return current_node.data

    def get_item_value(self, value):
        if self.head.data == value:
            return self.head.value
        else:
            while current is not None:
                if current.data == value:
                    return current
                else:
                    current = current.next
            return None

    # return the size
    def get_size(self):
        count = 0
        if self.head is None:
            return count
        else:
            current_node = self.head
            if current_node.next is None:
                count += 1
                return count
            else:
                while current_node.next is not None:
                    count += 1
                    current_node = current_node.next
                count += 1
                return count

    # print all items in the list
    def __str__(self):
        output = ""
        current_node = self.head
        while current_node.next is not None:
            output += f"{current_node.data}\t"
            current_node = current_node.next
        output += f"{current_node.data}"
        return output


if __name__ == '__main__':
    n1 = Node("node 1")
    n2 = Node("node 2")

    ll = LinkedList()
    ll.insert(n1.data)
    ll.insert(n2.data)
    print(ll)
    ll.insert("node 3")
    ll.insert("node 4")
    ll.insert("node 5")
    print(ll)
    ll.remove_index(0)
    ll.insert_at(1, "new node")
    print(f"Size is : {ll.get_size()}")
    print(ll)
    ll.insert_at(0, 'new head')
    print(f"Size is : {ll.get_size()}")
    print(ll)
    ll.remove_value('node 5')
    print(ll)
    ll.remove_value('new head')
    print(ll)
    ll.remove_value('node 2')
    print(ll)
    ll.remove_value('node 3')
    print(ll)
    ll.remove_value('node 5')
    print(ll)
    print(ll.get_size())