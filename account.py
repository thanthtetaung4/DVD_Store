import sqlite3


class Account:
    def __init__(self):
        self.username = str(self.login())

    def login(self):
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
            try:
                pwd = cur_obj.fetchone()[0]
            except:
                print('Wrong User Name')
                pwd = None
            else:
                count += 1
        # print(pwd)
        con.close()
        password = input("Password:")
        while password != pwd:
            print("Wrong password")
            password = input("Password:")
        return user_name


if __name__ == '__main__':
    authenticator = Account()
    print(type(authenticator.username))