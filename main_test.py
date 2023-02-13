from customer import Customer
import datetime
from dvd_list import DvDList
from dvd import DVD
from customer_list import CustomerList


def main():
    rented_date = datetime.date(2023, 2, 1)
    customer = Customer("fname", "lname", "123456",
                        {'dvd_00001': rented_date, 'dvd_00002': rented_date, 'dvd_00003': rented_date})
    customer2 = Customer("fname", "lname", "123457",
                         {'dvd_00001': rented_date, 'dvd_00002': rented_date, 'dvd_00003': rented_date})

    dvd_2 = DVD('dvd_00001', 'Interstellar', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, 'released_date')
    dvd_1 = DVD('dvd_00002', 'Your Name', ["1", "2", "3", "4", "5"], 'asdf', 'jkl', 'qwerty', 10, 'released_date')

    dvds = DvDList()
    dvds.insert(dvd_2)
    dvds.insert(dvd_1)
    # print(dvds)

    customers = CustomerList()
    customers.insert(customer)
    customers.insert(customer2)
    # print(customers)
    account_number = customer.get_account_number()
    print(dvd_return(account_number, customers, dvds))
    # dvd_rent('Interstellar', dvds, account_number, customers)
    # print(dvds , '-'*30, customers)


def dvd_return(account_number, customers, dvds):
    rented_dvd = dvds.find_dvd(input("Enter dvd name you want to return: "))
    dvd_id = rented_dvd.get_dvd_id()
    customer = customers.find_customer(account_number)
    customer_rented_dvds = customer.data.get_dvd_list()
    keys = []
    for key in customer_rented_dvds.keys():
        keys.append(key)
    for i in range(len(keys)):
        if dvd_id == keys[i]:
            rented_dvd.set_copies(rented_dvd.get_copies() + 1)
            fee = fee_calculator((datetime.date.today() - customer_rented_dvds[dvd_id]).days)
            customer.data.get_dvd_list().pop(dvd_id)
            return fee
        else:
            print('You did not rent that movie!')


def dvd_rent(dvd_name, dvds, account_number, customers):
    rented_dvd = dvds.find_dvd(dvd_name)
    if rented_dvd.get_copies() < 1:
        print(f"Sorry we have no copy left for {dvd_name}!")
        return False
    customer = customers.find_customer(account_number)
    customer_rented_dvds = customer.data.get_dvd_list()
    keys = []
    for key in customer_rented_dvds.keys():
        if key == rented_dvd.get_dvd_id():
            print(f"You cannot rent two copies of {dvd_name} at the same time!")
            return False
    rented_dvd.set_copies(rented_dvd.get_copies() - 1)
    customer.data.get_dvd_list()[rented_dvd.get_dvd_id()] = datetime.date.today()
    return True

def fee_calculator(days):
    normal_fee = 3
    if days > 7:
        fee = normal_fee * (days - 7) * 0.3
    return str(round(fee, 2)) + '$'

if __name__ == '__main__':
    main()
