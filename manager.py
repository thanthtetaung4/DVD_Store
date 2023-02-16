import datetime

from dvd_list import *
from customer_list import *
import sqlite3
import re

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

                            if dvd_detail[i] != '-':
                                temp2 += dvd_detail[i]
                            elif dvd_detail[i] == '-':
                                rented_date.append(temp2)
                                temp2 = ''
                    rented_date.append(temp2)
                    # print(dvd_id, rented_date)
                    date = datetime.date(int(rented_date[0]), int(rented_date[1]), int(rented_date[2]))
                    dvd_dict[dvd_id] = date
            elif char == ',':
                # print('detail_1', dvd_detail)
                for i in range(len(dvd_detail)):
                    if i < 9:
                        dvd_id += dvd_detail[i]
                    if i > 9:

                        if dvd_detail[i] != '-':
                            temp2 += dvd_detail[i]
                        elif dvd_detail[i] == '-':
                            rented_date.append(temp2)
                            temp2 = ''
                rented_date.append(temp2)
                # print('dvd,date', dvd_id, temp2)
                date = datetime.date(int(rented_date[0]), int(rented_date[1]), int(rented_date[2]))
                dvd_dict[dvd_id] = date
                dvd_id = ''
                rented_date = []
                dvd_detail = ''
                temp2 = ''
            count += 1
    # print(dvd_dict)
    return dvd_dict


class Manager:
    def __init__(self):
        self.dvds = DvDList()
        self.customers = CustomerList()
        self.get_dvds_from_db()
        self.get_customers_from_db()

    def get_dvds(self):
        return self.dvds

    def get_customers(self):
        return self.customers

    def get_dvds_from_db(self):
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        query = 'SELECT * from dvd order by movie_name'
        cur_obj = cur.execute(query)
        dvds_container = cur_obj.fetchall()

        dvds = []
        for dvd in dvds_container:
            dvds.append(dvd)

        for dvd in dvds:
            # print(dvd)
            stars = []
            temp = ''
            for char in dvd[2]:
                if char != ',':
                    temp += char
                else:
                    stars.append(temp)
                    temp = ''
            stars.append(temp)
            # print(DVD(dvd[1],dvd[0],stars,dvd[3],dvd[6],dvd[4],dvd[7],dvd[5]))
            self.dvds.insert(DVD(dvd[1], dvd[0], stars, dvd[3], dvd[6], dvd[4], dvd[7], dvd[5]))
        con.close()
        return True

    def get_customers_from_db(self):

        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur_obj = cur.execute("SELECT * FROM customer order by account_number")
        customers_container = cur_obj.fetchall()
        customers = []
        for customer in customers_container:
            customers.append(customer)
        # print(customers)
        # print(customers[int(len(customers) / 2)])
        self.customers.insert(Customer(customers[int(len(customers) / 2)][0], customers[int(len(customers) / 2)][1],
                                       customers[int(len(customers) / 2)][2],
                                       dvd_dict_maker(customers[int(len(customers) / 2)][3])))
        customers.remove(customers[int(len(customers) / 2)])
        for customer in customers:
            # print(customer)
            if customer[3] is None:
                self.customers.insert(Customer(customer[0], customer[1], customer[2], {}))
            else:
                self.customers.insert(Customer(customer[0], customer[1], customer[2], dvd_dict_maker(customer[3])))
        con.close()
        return True

    def dvd_return(self, account_number, customers, dvds):
        rented_dvd = dvds.find_dvd_customer(input("Enter dvd name you want to return: "))
        # print(rented_dvd)
        try:
            dvd_id = rented_dvd.get_dvd_id()
        except:
            return 'Wrong Input'
        # print(account_number)
        customer = customers.find_customer(account_number)
        # print(customer)
        customer_rented_dvds = customer.data.get_dvd_list()
        keys = []
        for key in customer_rented_dvds.keys():
            keys.append(key)
        # print(keys)
        # print(dvd_id)
        for i in range(len(keys)):
            # print(i)
            if dvd_id == keys[i]:
                rented_dvd.set_copies(rented_dvd.get_copies() + 1)
                fee = self.fee_calculator((datetime.date.today() - customer_rented_dvds[dvd_id]).days)
                customer.data.get_dvd_list().pop(dvd_id)
                dvd_list = self.dict_to_str(customer.data.get_dvd_list())
                con = sqlite3.connect(r"database/dvd_store.db")
                cur = con.cursor()
                cur.execute(
                    "UPDATE customer set dvd_list = '" + dvd_list + "' where account_number = '" + account_number + "';")
                cur.execute("UPDATE dvd set copies = '" + str(
                    rented_dvd.get_copies()) + "' where dvd_id = '" + rented_dvd.get_dvd_id() + "';")
                con.commit()
                con.close()
                return 'Rent fee is: ' + fee

        return 'You did not rent that movie!'

    def dvd_rent(self, dvd_name, dvds, account_number, customers):
        rented_dvd = dvds.find_dvd_customer(dvd_name)
        print()
        if rented_dvd.get_copies() < 1:
            return f"Sorry we have no copy left for {dvd_name}!"
        customer = customers.find_customer(account_number)
        customer_rented_dvds = customer.data.get_dvd_list()
        keys = []
        for key in customer_rented_dvds.keys():
            if key == rented_dvd.get_dvd_id():
                return f"You cannot rent two copies of {dvd_name} at the same time!"
        rented_dvd.set_copies(rented_dvd.get_copies() - 1)
        customer.data.get_dvd_list()[rented_dvd.get_dvd_id()] = datetime.date.today()
        dvd_list = self.dict_to_str(customer.data.get_dvd_list())
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur.execute(
            "UPDATE customer set dvd_list = '" + dvd_list + "' where account_number = '" + account_number + "';")
        cur.execute("UPDATE dvd set copies = '" + str(
            rented_dvd.get_copies()) + "' where dvd_id = '" + rented_dvd.get_dvd_id() + "';")
        con.commit()
        con.close()
        return "Don't forget to return after a week :)"

    def dict_to_str(self, dict):
        strr = ''
        keys = []
        values = []
        for key in dict.keys():
            keys.append(key)
        for value in dict.values():
            values.append(value)
        for i in range(len(keys)):
            strr += keys[i] + ':' + str(values[i]) + ','
        strr = strr[0:len(strr) - 1]
        return strr

    def dvd_id_generator(self):
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur_obj = cur.execute('select dvd_id from dvd order by dvd_id')
        ids = cur_obj.fetchall()
        # print(ids)
        # print(len(ids))
        current_id = 1
        new_id = None
        # print(ids[1][0][4:9])
        for i in range(len(ids)):
            # print('from list',int(ids[i][0][4:9]))
            # print('current', current_id)
            if int(ids[i][0][4:9]) > current_id:
                new_id = str(current_id)
                # print(i)
            else:
                # print(i)
                current_id += 1
                i += 1
        if new_id is None and int(ids[len(ids) - 1][0][4:9]) + 1 < 99999:
            new_id = str(int(ids[len(ids) - 1][0][4:9]) + 1)
        elif int(ids[len(ids) - 1][0][4:9]) + 1 > 99999:
            return False
        con.close()
        return 'dvd_' + '0' * (len(ids[len(ids) - 1][0]) - 5) + new_id

    def customer_id_generator(self):
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur_obj = cur.execute('select account_number from customer order by account_number')
        ids = cur_obj.fetchall()
        con.close()
        current_id = 1111
        new_id = None
        for i in range(len(ids)):
            if int(ids[i][0]) > current_id:
                new_id = current_id
                # print(i)
            else:
                # print(i)
                current_id += 1
                i += 1
        if new_id is None and int(ids[len(ids) - 1][0]) + 1 < 9999:
            new_id = int(ids[len(ids) - 1][0]) + 1
        elif int(ids[len(ids) - 1][0]) + 1 > 9999:
            return False
        return str(new_id)


    def add_dvd(self):
        movie_name = input("Enter movie name: \t")
        stars = input("Enter Stars:\t")
        producer = input("Enter Producer:\t")
        director = input("Enter Director:\t")
        company = input("Enter Company:\t")
        copies = (input("Enter Copies:\t"))
        released_date = input("Enter Released Date:\t")
        dvd_id = self.dvd_id_generator()
        query = "insert into dvd (movie_name, dvd_id, stars, producer, company, released_data, director, copies) values ('" + movie_name + "','" + dvd_id + "','" + stars + "','" + producer + "','" + company + "','" + released_date + "','" + director + "','" + copies + "');"
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur.execute(query)
        if input('ARE YOU SURE ABOUT ADDING' + movie_name + ' TO DATABASE ? \nInput 1 To COMMIT\nInput any to STOP\n>>>>>\t') == '1':

            if self.dvds.insert(DVD(dvd_id, movie_name, stars, producer, director, company, copies, released_date)):
                con.commit()
                print(movie_name + '\nAdded to DB!\n')
            else:
                print('unsuccessful\n')
        else:
            con.close()
            return
        con.close()

    def delete_dvd(self):
        dvd_id = input("Enter ID of DVD you want to delete:\t")
        deleted_dvd = None
        for dvd in self.dvds.convert_to_list():
            if dvd.data.get_dvd_id() == dvd_id:
                deleted_dvd = dvd
        if deleted_dvd is not None:
            query = "DELETE FROM dvd where dvd_id = '" + dvd_id + "';"
            con = sqlite3.connect(r"database/dvd_store.db")
            cur = con.cursor()
            cur.execute(query)
            if input('ARE YOU SURE ABOUT DELETING ' + deleted_dvd.data.get_movie_name() + ' FROM DATABASE ? \nInput 1 To COMMIT\nInput any to STOP\n>>>>>\t') == '1':
                print(deleted_dvd.data.get_movie_name() + '\nDeleted from DB!')
                self.dvds.delete_dvd(dvd_id)
                con.commit()
            else:
                con.close()
                return
            con.close()
        else:
            print('DVD does not exist')

    def delete_customer(self):
        account_number = input("Enter Account Number of customer you want to delete:\t")
        deleted_customer = None
        for customer in self.customers.convert_to_list():
            if customer.get_account_number() == str(account_number):
                deleted_customer = customer
        if deleted_customer is not None:
            query = "DELETE FROM customer where account_number = '" + account_number + "';"
            con = sqlite3.connect(r"database/dvd_store.db")
            cur = con.cursor()
            cur.execute(query)
            query = "DELETE FROM user_account where account_number = '" + account_number + "';"
            cur.execute(query)
            if input('ARE YOU SURE ABOUT DELETING ' + deleted_customer.get_name() + ' FROM DATABASE ? \nInput 1 To COMMIT\nInput any to STOP\n>>>>>\t') == '1':
                msg = 'Name:'+ deleted_customer.get_name() + '\nAccount Number:' + account_number + '\nis Deleted from DB!'
                print(msg)
                if self.customers.delete_cutomer(account_number):
                    con.commit()
                else:
                    print('unsuccessful\n')
            else:
                con.close()
                return
            con.close()
        else:
            print('Customer does not exist')

    def add_customer(self):
        fname = input("Enter first name\n")
        lname = input("Enter last name\n")
        account_number = self.customer_id_generator()
        new_customer = Customer(fname, lname, account_number, {})
        self.customers.insert(Customer(fname, lname, account_number, {}))
        query = "insert into customer (first_name, last_name, account_number) values ('" + fname + "','" + lname + "','" + account_number + "');"
        con = sqlite3.connect(r"database/dvd_store.db")
        cur = con.cursor()
        cur.execute(query)
        query = "insert into user_account (account_number, password) values ('" + account_number + "', 12345);"
        cur.execute(query)
        if input('ARE YOU SURE ABOUT ADDING ' + new_customer.get_name() + ' TO DATABASE ? \nInput 1 To COMMIT\nInput any to STOP\n>>>>>\t') == '1':
            print(new_customer.get_name() + '\nAdded to DB!')
            con.commit()
        else:
            con.close()
            return
        con.close()

    def find_dvd_customer(self):
        dvd_name = input("Enter DVD name you want to search:\t")
        temp = re.split('\n',self.dvds.find_dvd(dvd_name).__str__())
        temp.pop(0)
        dvd_detail = ''
        for line in temp:
            dvd_detail += line + '\n'
        return dvd_detail

    def find_dvd_admin(self):
        dvd_name = input("Enter DVD name you want to search:\t")
        return self.dvds.find_dvd(dvd_name)
    def customer_dvd_inter(self, dvd):
        temp = re.split('\n', dvd.__str__())
        temp.pop(0)
        dvd_detail = ''
        for line in temp:
            dvd_detail += line + '\n'
        return dvd_detail


    def find_dvds_rented_by_customer_admin(self):
        account_number = input('Enter account number:\t')
        dvd_list = self.customers.find_customer(account_number).data.get_dvd_list()
        keys = []
        for key in dvd_list.keys():
            keys.append(key)
        values = []
        for value in dvd_list.values():
            values.append(value)
        dvds_rented_by_customer = ''
        if len(keys) == 0:
            return 'No DVD rented\n'
        for i in range(len(keys)):
            dvd_name = self.dvds.find_at(i).get_movie_name()
            dvds_rented_by_customer += dvd_name + " due at " + str(values[i] + datetime.timedelta(days=7)) + "\n"
        return dvds_rented_by_customer

    def find_dvds_rented_by_customer_user(self, account_number):
        dvd_list = self.customers.find_customer(account_number).data.get_dvd_list()
        keys = []
        for key in dvd_list.keys():
            keys.append(key)
        values = []
        for value in dvd_list.values():
            values.append(value)
        dvds_rented_by_customer = ''
        if len(keys) == 0:
            return 'No DVD rented\n'
        for i in range(len(keys)):
            dvd_name = self.dvds.find_at(i).get_movie_name()
            dvds_rented_by_customer += dvd_name + " due at " + str(values[i] + datetime.timedelta(days=7)) + "\n"
        return dvds_rented_by_customer

    def fee_calculator(self, days):
        normal_fee = 3

        if days > 7:
            total_fee = normal_fee * (days - 7) * 0.3
            return str(round(total_fee, 2)) + '$'
        return str(normal_fee) + '$'

    def get_due_soon(self):
        msg = 'Due Soon'

        for customer in self.customers.convert_to_list():
            customer_dvd_list = customer.get_dvd_list()

            if len(customer_dvd_list) > 0:
                count = 0
                for key in customer_dvd_list.keys():
                    if (datetime.date.today() - customer_dvd_list[key]).days > 4:
                        if count == 0:
                            msg += '\n\n' + customer.get_name()
                            count += 1
                        for dvd in self.dvds.convert_to_list():
                            if dvd.data.get_dvd_id() == key:
                                 msg += '\n"' + dvd.data.get_movie_name() + '" due at ' + str(customer_dvd_list[key] + datetime.timedelta(days=7))
        return msg + '\n'

if __name__ == '__main__':
    manager = Manager()

    dvds = manager.get_dvds()
    customers = manager.get_customers()

    # print(dvds)
    # print(customers)
    # print(dvds.find_dvd('Interstellar'))
    # print(manager.dvd_return('1234', customers, dvds))
    # manager.add_dvd()
    # print(dvds)
    # manager.add_customer()
    # print(customers)
    # manager.delete_dvd()
    # print(dvds)
    # manager.delete_customer()
    # print(customers)
    # print(manager.find_dvd())
    # print(manager.find_dvds_rented_by_customer_admin())
