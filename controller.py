
import customer
import account
import account_logic
import transaction_table


def create_tables_if_not_exists():
    customer.create_table()
    account.create_table()
    transaction_table.create_table()


def insert_into_table(table_name, insert_dict):
    if table_name == "customer":
        customer.insert(insert_dict)
    elif table_name == "account":
        insert_dict['account_number'] = account_logic.generate_unique_account_number()
        account.insert(insert_dict)
    elif table_name == "transaction_details":
        transaction_table.insert(insert_dict)
    else:
        raise Exception("Invalid name of table")


def fetch_all_from_table(table_name):
    record = None
    if table_name == "customer":
        record = customer.fetch_all()
    elif table_name == "account":
        record = account.fetch_all()
    elif table_name == "transaction_details":
        record = transaction_table.fetch_all()
    else:
        raise Exception("Invalid name of table")

    return record


def fetch_one_from_table(id, table_name):
    record = None
    if table_name == "customer":
        record = customer.fetch_one_with_customer_id(id)
    elif table_name == "account":
        record = account.fetch_one_with_account_number(id)
    elif table_name == "transaction_detail":
        record = transaction_table.fetch_one_with_transaction_id(id)
    else:
        raise Exception("Invalid name of table")

    return record


def update_in_table(table_name, update_dict):
    if table_name == "customer":
        customer.update(update_dict)
    elif table_name == "account":
        account.update(update_dict)
    elif table_name == "transaction_detail":
        transaction_table.update(update_dict)
    else:
        raise Exception("Invalid name of table")


def delete_one_from_table(table_name, id):
    if table_name == "customer":
        customer.delete_one_with_customer_id(id)
    elif table_name == "account":
        account.delete_one_with_account_number(id)
    elif table_name == "transaction_detail":
        transaction_table.delete_one_with_transaction_id(id)
    else:
        raise Exception("Invalid name of table")

