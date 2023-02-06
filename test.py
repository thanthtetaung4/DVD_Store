# methods in this file are still in testing

from datetime import date


def generate_bill(date):
    fee = 3
    today = date.today()
    days = today - date
    bill = fee
    if days.days > 7:
        bill = bill + (fee * 0.2) * days.days
    return str(round(bill, 2)) + '$'


def delete_from_dict(dict, dvd_name):
    del dict[dvd_name]
    return True


def main():
    date1 = date(2023, 1, 10)
    date2 = date(2023, 2, 1)

    new_dict = {"Fantastic Beasts and Where to Find Them": date1, "A Silent Voice": date2}
    print(generate_bill(date1))
    delete_from_dict(new_dict, 'A Silent Voice')
    print(new_dict)

    name = 'Thbnt Htet Aung'
    name2 = 'Aung Htet Thant'
    name3 = 'Thant Htet Aungh'
    print(name < name3)


if __name__ == '__main__':
    main()
