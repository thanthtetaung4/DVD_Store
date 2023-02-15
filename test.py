# methods in this file are still in testing

from datetime import date
import sqlite3


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

    [a, b] = 1, 2
    print(a)
    print(b)

    # con = sqlite3.connect(r"C:\sqlite\customer.db")
    # cur = con.cursor()
    # # cur.execute("CREATE TABLE movie(title, year, score)")
    # # res = cur.execute("SELECT name FROM sqlite_master")
    # # print(res.fetchone())
    # cur.execute("""
    #     INSERT INTO movie VALUES
    #         ('a', 1975, 8.2),
    #         ('b', 1971, 7.5)
    # """)
    # con.commit()
    # res = cur.execute("SELECT * FROM movie")
    # print(res.fetchall())
if __name__ == '__main__':
    print(True)


