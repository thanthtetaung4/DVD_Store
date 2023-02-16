from customer import Customer
import datetime
import sqlite3

def main():
    # rented_date = datetime.date(2023, 2, 1)
    # customer = Customer("fname", "lname", "123456",
    #                     {'dvd_00001': rented_date, 'dvd_00002': rented_date, 'dvd_00003': rented_date})
    # customer2 = Customer("fname", "lname", "123457",
    #                      {'dvd_00001': rented_date, 'dvd_00002': rented_date, 'dvd_00003': rented_date})
    #
    # print(customer)
    # keys = []
    # values = []
    # print(customer.dvd_list.keys(), customer.dvd_list.values())
    # for key in customer.dvd_list.keys():
    #     keys.append(key)
    # print(keys)
    # for value in customer.dvd_list.values():
    #     values.append(value)
    # print(values)
    # today = datetime.date.today()
    # print((today - values[0]).days)
    # print(fee_calculator((today - values[0]).days))
    today = datetime.date.today()
    print(today)
    dict = {'a': today, 'b' : today}
    strr = ''
    keys = []
    values = []
    for key in dict.keys():
        keys.append(key)
    for value in dict.values():
        values.append(value)
    for i in range(len(keys)):
        strr += keys[i] + ':' + str(values[i]) + ','
    strr = strr[0:len(strr)-1]
    print(strr)
def dvd_id_generator():
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
            i +=1
    if new_id is None and int(ids[len(ids)-1][0][4:9]) + 1 > 99999:
        new_id = str(int(ids[len(ids)-1][0][4:9]) + 1)
    if int(ids[len(ids)-1][0][4:9]) + 1 > 99999:
        return False
    con.close()
    return 'dvd_' + '0' * (len(ids[len(ids)-1][0]) - 5) + new_id
def customer_id_generator():
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
    if new_id is None and int(ids[len(ids)-1][0])+1 < 9999:
        new_id = int(ids[len(ids)-1][0])+1
    return new_id

def fee_calculator(days):
    normal_fee = 3
    if days > 7:
        fee = normal_fee * (days - 7) * 0.3
    return str(round(fee, 2)) + '$'


if __name__ == '__main__':
    # main()
    # list = [1,2,3,4,5,6,7,8,9]
    # value = 2
    # print(list[binary_search(list, value)])
    print(dvd_id_generator())
    print(customer_id_generator())
