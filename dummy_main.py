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
               "7. See DVDs rented by Customer\n" \
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
            elif option == '7':
                manager.find_dvds_rented_by_customer_admin()
            else:
                print('Wrong Input!')

            option = input(menu)
    else:
        menu = "1. Rent DVD\n" \
               "2. Return DVD\n" \
               "3. See Your Rented DVDs\n" \
               "'$' to Quit\n" \
               ">>>>>\t"
        option = input(menu)
        while option != '$':
            if option == '1':
                dvd_list = manager.get_dvds().get_dvd_names()
                # print(dvd_list)
                menu_2 = "1. To Find a movie\n" \
                         "2. To See all available movies\n" \
                         "'$' To Back\n" \
                         ">>>>>\t"
                option_2 = input(menu_2)
                while option_2 != '$':
                    if option_2 == '1':
                        find_dvd = manager.find_dvd()
                        print(find_dvd)
                        menu_4 = "1 to rent\n" \
                                 "'$' to back to previous menu\n"
                        option_4 = input(menu_4)
                        while option_4 != '$':
                            if option_4 == '1':
                                print(manager.dvd_rent(find_dvd.get_movie_name(),
                                                       dvds, user_name.username, customers))
                            option_4 = input(menu_4)
                    elif option_2 == '2':
                        menu_3 = ''
                        for index, dvd in enumerate(dvd_list):
                            menu_3 += str(index + 1) + '.' + dvd + '\n'
                        menu_3 += "Enter '$' to Back\n" \
                                  "Enter number in front of dvd to see details\n"
                        option_3 = input(menu_3)
                        while option_3 != '$':
                            try:
                                if 0 < int(option_3) < dvds.get_dvd_list().get_size() + 1:
                                    print(dvds.find_at(int(option_3) - 1))

                                    menu_4 = "1 to rent\n" \
                                             "'$' to back to previous menu\n"
                                    option_4 = input(menu_4)
                                    while option_4 != '$':
                                        if option_4 == '1':
                                            print(manager.dvd_rent(dvds.find_at(int(option_3) - 1).get_movie_name(),
                                                                   dvds, user_name.username, customers))
                                            break
                                        option_4 = input(menu_4)
                                option_3 = input(menu_3)
                            except ValueError:
                                print("Wrong Input!")
                                option_3 = input(menu_3)
                    option_2 = input(menu_2)
            elif option == '2':
                print(manager.dvd_return(str(user_name.username), manager.get_customers(), manager.get_dvds()))
            elif option == '3':
                print(manager.find_dvds_rented_by_customer_user(str(user_name.username)))
            option = input(menu)
        print("Thank You So Much For Using Our System\n")


if __name__ == '__main__':
    main()
