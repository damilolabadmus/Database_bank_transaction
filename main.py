
from controller import *


def print_menu():
    print('\nWelcome to tha Banking Application')
    menu = (""" 1. View Customers 2. View Accounts 3. View Transactions 4. Add New Customer 5. Add New Account 6. Add New Transaction 7. Update Customer Record 8. Update Account Record  
                9. Delete a Customer Record 10. Delete an Account 11. Delete a Transaction Record """)
    print(menu)


def print_records(records):
    if records:
        for record in records:
            print()
            for row in record:
                print(row)
            print()
    else:
        print("Empty")


def get_customer_input_details(take_id=False):
    customer_dict = {
        'first_name': '',
        'last_name': '',
        'middle_name': '',
        'mobile_number': '',
        'occupation': '',
        'date_of_birth': ''
    }

    if take_id:
        customer_dict['customer_id'] = ' '

    for key in customer_dict:
        prompt = "Enter " + str(key).replace('_', ' ').capitalize() + ": "
        customer_dict[key] = input(prompt)

    return customer_dict


def get_account_input_details(take_id=False):
    account_dict = {
        'customer_id': '',
        'account_opening_date': '',
        'account_type': '',
        'account_status': ''
    }

    if take_id:
        account_dict['account_number'] = ' '

    for key in account_dict:
        prompt = "Enter " + str(key).replace('_', ' ').capitalize() + ": "
        account_dict[key] = input(prompt)

    return account_dict


def get_transaction_input_details():
    transaction_dict = {
        'account_number': '',
        'transaction_date': '',
        'transaction_type': '',
        'transaction_amount': '',
        'transaction_medium': ''
    }

    for key in transaction_dict:
        prompt = "Enter " + str(key).replace('_', ' ').capitalize() + ": "
        transaction_dict[key] = input(prompt)

    return transaction_dict


def run_banking_application():
    while True:
        print_menu()
        option = int(input("Enter menu option, Enter -1 to end: "))

        if option == 1:
            print_records(fetch_all_from_table("customer"))
        elif option == 2:
            print_records(fetch_all_from_table("account"))
        elif option == 3:
            print_records(fetch_all_from_table("transaction_details"))
        elif option == 4:
            insert_into_table("customer", get_customer_input_details())
        elif option == 5:
            insert_into_table("account", get_account_input_details())
        elif option == 6:
            insert_into_table("transaction_details", get_transaction_input_details())
        elif option == 7:
            update_in_table("customer", get_customer_input_details(take_id=True))
        elif option == 8:
            update_in_table("account", get_account_input_details(take_id=True))
        elif option == 9:
            delete_one_from_table("customer", input("Enter ID of customer record to delete: "))
        elif option == 10:
            delete_one_from_table("account", input("Enter account number to delete: "))
        elif option == 11:
            delete_one_from_table("transaction_detail", input("Enter ID of transaction record to delete: "))
        else:
            break


def main():
    create_tables_if_not_exists()
    run_banking_application()


if __name__ == '__main__':
    main()
