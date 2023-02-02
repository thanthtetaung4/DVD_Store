from linked_list import LinkedList
class Customer:
    def __init__(self, fname, lname, account_number, dvd_list):
        self.fist_name = fname
        self.last_name = lname
        self.account_number = account_number
        self.dvd_list = dvd_list

    def __str__(self):
        dvds = ''
        for dvd in self.dvd_list:
            dvds += f"{dvd} "
        output = f"First Name: {self.fist_name}\n" \
                 f"Last Name: {self.last_name}\n" \
                 f"Account Number: {self.account_number}\n" \
                 f"DVD List: {dvds}\n"
        return output

if __name__ == '__main__':
    customer = Customer("fname","lname", "123456", ['dvd1', 'dvd2', 'dvd3'])
    print(customer)

