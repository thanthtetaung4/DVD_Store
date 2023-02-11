class Customer:
    def __init__(self, fname, lname, account_number, dvd_list):
        self.fist_name = fname
        self.last_name = lname
        self.account_number = account_number
        self.dvd_list = dvd_list  # {dvd name : rented date} => dictionary

    def get_name(self):
        return self.fist_name + self.last_name

    def get_first_name(self):
        return self.fist_name

    def get_last_name(self):
        return self.last_name

    def get_account_number(self):
        return self.account_number

    def get_dvd_list(self):
        return self.dvd_list

    def set_name(self, fname, lname):
        self.fist_name = fname
        self.last_name = lname

    def set_first_name(self, fname):
        self.fist_name = fname

    def set_last_name(self, lanme):
        self.last_name = lname

    # no set for account number unchangable
    def set_dvd_list(self, dvd_list):
        self.dvd_list = dvd_list

    def __lt__(self, other):
        if type(other) is str:
            return self.get_account_number() < other
        return self.get_account_number() < other.get_account_number()
    def __gt__(self, other):
        if type(other) is str:
            return self.get_account_number() > other
        return self.get_account_number() > other.get_account_number()
    def __eq__(self, other):
        if type(other) is str:
            return self.get_account_number() == other
        return self.get_account_number() == other.get_account_number()

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
    customer = Customer("fname", "lname", "123456", ['dvd1', 'dvd2', 'dvd3'])
    customer2 = Customer("fname", "lname", "123457", ['dvd1', 'dvd2', 'dvd3'])
    print('123458' > customer2)
    number = '123457'
    print(number == customer2)
    print(customer)
