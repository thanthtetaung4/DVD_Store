from customer import Customer
import datetime


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


def fee_calculator(days):
    normal_fee = 3
    if days > 7:
        fee = normal_fee * (days - 7) * 0.3
    return str(round(fee, 2)) + '$'


if __name__ == '__main__':
    main()
