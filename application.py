from dvd_list import *
from customer import *
from account import Account
from manager import Manager


def main():
    user_name = Account()
    manager = Manager()
    dvds = manager.get_dvds()
    customers = manager.get_customers()
    # print(customers)
    if user_name.username == "0000":
        menu = "1. See All Customers\n" \
               "2. See All DVDs\n" \
               "3. Add DVD\n" \
               "4. Delete DVD\n" \
               "5. Add Customer\n" \
               "6. Delete Customer\n" \
               "'$' To Exit\n" \
               ">>>>>\t" \

        option = input(menu)
        while option != '$':
            if option == '1':
                print(customers)
            elif option == '2':
                print(dvds)
            elif option == '3':
                manager.add_dvd()
            elif option == '4':
                manager.delete_dvd()
            elif option == '5':
                manager.add_customer()
            elif option == '6':
                manager.delete_customer()

            option = input(menu)
    else:
        menu = "1.Rent DVD\n" \
               "2.Return DVD\n" \
               "Enter $ to Quit\n"
        option = input(menu)
        while option != '$':
            if option == '1':
                dvd_list = manager.get_dvds().get_dvd_names()
                # print(dvd_list)
                menu_2 = ''
                for index, dvd in enumerate(dvd_list):
                    menu_2 += str(index + 1) + '.' + dvd + '\n'
                menu_2 += "Enter '$' to Back\n" \
                          "Enter number in front of dvd to see details\n"
                option_2 = input(menu_2)
                while option_2 != '$':
                    if 0 < int(option_2) < dvds.get_dvd_list().get_size() +1 :
                        print(dvds.find_at(int(option_2)-1))

                        menu_3 = "1 to rent\n" \
                                 "'$' to back to previous menu\n"
                        option_3 = input(menu_3)
                        while option_3 != '$':
                            if option_3 == '1':
                                print(manager.dvd_rent(dvds.find_at(int(option_2)-1).get_movie_name(),
                                                       dvds, user_name.username, customers))

                            option_3 = input(menu_3)


                    option_2 = input(menu_2)

            elif option == '2':
                print(manager.dvd_return(str(user_name.username), manager.get_customers(), manager.get_dvds()))

            option = input(menu)
        print("Thank You So Much For Using Our System\n")


if __name__ == '__main__':
    main()
