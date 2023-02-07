from dvd import DVD
from linked_list import LinkedList
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

    def find_dvd(self, dvd_name):
        # use the best searching algorithm for linked list which is linear search because the traversal of LL can't
        # be improved from O(n)
        current_node = self.dvd_list.head
        while current_node.next is not None:
            if current_node.data.get_movie_name() == dvd_name:
                return current_node.data
            else:
                current_node = current_node.next
        return f"{dvd_name} is not in your store. Sorry for inconvenience :("

    def __str__(self):
        output = ""
        current_node = self.dvd_list.head
        while current_node.next is not None:
            output += f"{current_node.data}\n"
            current_node = current_node.next
        output += f"{current_node.data}"
        return output


if __name__ == '__main__':
    released_date = datetime.date.today()
    dvd_2 = DVD('Interstellar', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, released_date)
    dvd_1 = DVD('Your Name', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, released_date)
    dvd_3 = DVD('A Silent Voice', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, released_date)
    dvd_4 = DVD('Fantastic Beasts and Where to Find Them', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, released_date)
    dvds = DvDList()
    t1 = datetime.datetime.now()
    dvds.insert(dvd_2)
    dvds.insert(dvd_1)
    dvds.insert(dvd_3)
    dvds.insert(dvd_4)
    t2 = datetime.datetime.now()
    print(t1)
    print(t2)
    print('Time taken to insert data', t2 - t1, '\n')

    print(dvds)

    print(dvds.find_dvd('Fantastic Beasts and Where to Find Them'))
