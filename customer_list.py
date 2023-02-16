from customer import Customer
from binary_search_tree import BST
class CustomerList:
    def __init__(self):
        self.customer_list = BST()

    def insert(self, customer):
        self.customer_list.insert(customer)

    def get_customer(self, customer_name):
        # return a customer that has {customer_name} as name
        pass
    def find_max(self, account_number):
        return self.customer_list.find_max(account_number)
    def delete_cutomer(self, account_name):
        # remove a customer that has {customer_name} as name
        return self.customer_list.delete_node(self.find_customer(account_name))
    def lvl_order(self):
        return self.customer_list.level_order_traverse()
    def find_customer(self, account_number):
        # print('\nfind_customer\n',self.customer_list.get_node(account_number).data)
        return self.customer_list.get_node(account_number)
        # root = self.customer_list.root
        # while root is not None:
        #     if account_number == root.data:
        #         return root
        #     elif account_number < root.data:
        #         root = root.left
        #     else:
        #         root = root.right
        # return None
    def convert_to_list(self):
        result = []
        self.customer_list.in_order_traverse(self.customer_list.root,result)
        return result
    def update(self, customer_name):
        # update a customer that has {customer_name} as name with prompts to choose what file to change
        pass

    def __str__(self):
        # return all customers as str
        output = self.customer_list.__str__()

        return output


if __name__ == '__main__':
    customer_list = CustomerList()
    customer = Customer("fname", "lname", "010", ['dvd1', 'dvd2', 'dvd3'])
    customer2 = Customer("fname1", "lname2", "005", ['dvd1', 'dvd2', 'dvd3'])
    customer3 = Customer("fname1", "lname2", "015", ['dvd1', 'dvd2', 'dvd3'])
    customer4 = Customer("fname1", "lname2", "004", ['dvd1', 'dvd2', 'dvd3'])
    customer5 = Customer("fname1", "lname2", "006", ['dvd1', 'dvd2', 'dvd3'])
    customer6 = Customer("fname1", "lname2", "012", ['dvd1', 'dvd2', 'dvd3'])
    customer7 = Customer("fname1", "lname2", "016", ['dvd1', 'dvd2', 'dvd3'])
    customer_list.insert(customer)
    customer_list.insert(customer2)
    customer_list.insert(customer3)
    customer_list.insert(customer4)
    # customer_list.insert(customer5)
    customer_list.insert(customer6)
    customer_list.insert(customer7)
    # print(customer_list)
    # print(customer_list.find_customer('012').data)
    # print(customer_list.find_max(customer_list.find_customer('010')).data)
    print('='*20)
    customer_list.delete_cutomer('012')
    # print(customer_list)
    print(customer_list.customer_list.iod_print())