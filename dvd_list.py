from dvd import DVD
from linked_list import *


class DvDList:
    def __init__(self):
        self.dvd_list = LinkedList()

    def insert(self, dvd):
        index = 0
        if self.dvd_list.head is None:
            self.dvd_list.insert(dvd)
        else:
            print(type(self.dvd_list.head))
            current = self.dvd_list.head
            print(type(current))
            current_data = current.data




    def find_dvd(self, dvd):
        # use the best searching algorithm for linked list
        pass

    def __str__(self):
        output = str(self.dvd_list)
        return output

if __name__ == '__main__':

    dvd_2 = DVD('b', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvd_1 = DVD('a', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvd_3 = DVD('c', [1, 2, 3, 4, 5], 'asdf', 'jkl', 'qwerty', 10)
    dvds = DvDList()
    dvds.insert(dvd_2)
    dvds.insert(dvd_1)
    dvds.insert(dvd_3)
    print(dvds)
