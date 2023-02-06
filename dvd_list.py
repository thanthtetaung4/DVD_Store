from dvd import DVD
from linked_list import LinkedList
from node import Node
import datetime


class DvDList:
    def __init__(self):
        self.dvd_list = LinkedList()

    def insert(self, dvd):
        if self.dvd_list.head is None:
            self.dvd_list.insert(dvd)
        else:
            if self.dvd_list.get_size() == 1:
                if self.dvd_list.head.data.get_movie_name() > dvd.get_movie_name():
                    self.dvd_list.insert_at(0, dvd)
                else:
                    self.dvd_list.insert(dvd)
            else:
                current = self.dvd_list.head
                index = 0
                while current.next is not None:
                    if current.data.get_movie_name() > dvd.get_movie_name():
                        self.dvd_list.insert_at(index, dvd)
                        return True
                    else:
                        index += 1
                        current = current.next
                self.dvd_list.insert(dvd)

    def find_dvd(self, dvd):
        # use the best searching algorithm for linked list
        pass

    def __str__(self):
        output = ""
        current_node = self.dvd_list.head
        while current_node.next is not None:
            output += f"{current_node.data}\n"
            current_node = current_node.next
        output += f"{current_node.data}"
        return output


if __name__ == '__main__':
    dvd_2 = DVD('Interstellar', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvd_1 = DVD('Your Name', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvd_3 = DVD('A Silent Voice', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvd_4 = DVD('Fantastic Beasts and Where to Find Them', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvds = DvDList()
    t1 = datetime.datetime.now()
    dvds.insert(dvd_2)
    dvds.insert(dvd_1)
    dvds.insert(dvd_3)
    dvds.insert(dvd_4)
    t2 = datetime.datetime.now()
    print('Time taken to insert data', t2 - t1, '\n')
    print(dvds)
