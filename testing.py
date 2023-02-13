import sqlite3
import datetime
from customer import Customer
from customer_list import CustomerList


def main():
    get_customers_from_db()
    # login()


def login():
    con = sqlite3.connect(r"database/dvd_store.db")
    cur = con.cursor()
    pwd = None
    count = 0
    while pwd is None:
        if count > 0:
            print("Wrong username")
        user_name = input("User name (Account Number):")
        query = f"SELECT password from user_account WHERE account_number = '{user_name}'"
        # print(query)
        cur_obj = cur.execute(query)
        pwd = cur_obj.fetchone()[0]
        count += 1
    # print(pwd)
    con.close()
    password = input("Password:")
    while password != pwd:
        print("Wrong password")
        password = input("Password:")
    return user_name

def dvd_dict_maker(dvd_renting_details):
    dvd_detail = ''
    dvd_id = ''
    rented_date = []
    temp2 = ''
    dvd_dict = {}
    count = 0
    if dvd_renting_details is not None:
        for char in dvd_renting_details:
            # print(count)
            if char != ',':
                dvd_detail += char
                if count == len(dvd_renting_details) - 1:
                    # print('detail_2', dvd_detail)
                    for i in range(len(dvd_detail)):
                        if i < 9:
                            dvd_id += dvd_detail[i]
                        if i > 9:

                            if dvd_detail[i] != '/':
                                temp2 += dvd_detail[i]
                            elif dvd_detail[i] == '/':
                                rented_date.append(temp2)
                                temp2 = ''
                    rented_date.append(temp2)
                    # print(dvd_id, rented_date)
                    date = datetime.date(int(rented_date[2]), int(rented_date[1]), int(rented_date[0]))
                    dvd_dict[dvd_id] = date
            elif char == ',':
                # print('detail_1', dvd_detail)
                for i in range(len(dvd_detail)):
                    if i < 9:
                        dvd_id += dvd_detail[i]
                    if i > 9:

                        if dvd_detail[i] != '/':
                            temp2 += dvd_detail[i]
                        elif dvd_detail[i] == '/':
                            rented_date.append(temp2)
                            temp2 = ''
                rented_date.append(temp2)
                # print('dvd,date',dvd_id, temp2)
                date = datetime.date(int(rented_date[2]), int(rented_date[1]), int(rented_date[0]))
                dvd_dict[dvd_id] = date
                dvd_id = ''
                rented_date = []
                dvd_detail = ''
                temp2 = ''
            count += 1
    # print(dvd_dict)
    return dvd_dict

def get_customers_from_db():
    customer_list = CustomerList()
    con = sqlite3.connect(r"database/dvd_store.db")
    cur = con.cursor()
    cur_obj = cur.execute("SELECT * FROM customer order by account_number")
    customers_container = cur_obj.fetchall()
    customers = []
    for customer in customers_container:
        customers.append(customer)
    # print(customers)
    # print(customers[int(len(customers) / 2)])
    customer_list.insert(Customer(customers[int(len(customers) / 2)][0], customers[int(len(customers) / 2)][1],
                                  customers[int(len(customers) / 2)][2],
                                  dvd_dict_maker(customers[int(len(customers) / 2)][3])))
    customers.remove(customers[int(len(customers) / 2)])
    for customer in customers:
        print(customer)
        if customer[3] is None:
            customer_list.insert(Customer(customer[0], customer[1], customer[2], {}))
        else:
            customer_list.insert(Customer(customer[0], customer[1], customer[2], dvd_dict_maker(customer[3])))
    con.close()
    print(customer_list)
    print('=' * 30)
    # dummy_list = customer_list.lvl_order()
    # s = ''
    # for i in dummy_list:
    #     s += str(i.data) + '\n'
    # print(s)


if __name__ == '__main__':
    main()
