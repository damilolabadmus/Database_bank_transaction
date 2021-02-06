import bank_transaction
from mysql.connector import Error


def create_account_table():
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    create_sql = "CREATE TABLE if not exists account (" \
                 "account_number INTEGER NOT NULL," \
                 "customer_id INTEGER NOT NULL," \
                 "account_opening_date DATE," \
                 "account_type VARCHAR(10) NOT NULL," \
                 "account_status VARCHAR(10) NOT NULL," \
                 "CONSTRAINT account_pk PRIMARY KEY(account_number)," \
                 "CONSTRAINT account_fk1 FOREIGN KEY(customer_id) REFERENCES customer(customer_id)" \
                 ")"
    try:
        db_cursor.execute(create_sql)
        connection.commit()
        print("Your account table has been created")
        db_cursor.close()
    except Error as error:
        print("Error creating account table", error)
    finally:
        bank_transaction.close(connection)


def insert(new_account_dict):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    insert_sql = "insert into account (account_number, customer_id, account_opening_date, account_type, account_status) " \
                 "values (%s, %s, %s, %s, %s)"

    account_details = (
        new_account_dict['account_number'],
        new_account_dict['customer_id'],
        new_account_dict['account_opening_date'],
        new_account_dict['account_type'],
        new_account_dict['account_status']
    )

    try:
        db_cursor.execute(insert_sql, account_details)
        connection.commit()
        print(db_cursor.rowcount, "row has been inserted.")
        db_cursor.close()
    except Error as error:
        print("Error inserting row:", error)
    finally:
        bank_transaction.close(connection)


def fetch_one_with_account_number(account_number):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    select_sql = "select * from account where account_number = %s"
    account = None

    try:
        db_cursor.execute(select_sql, (account_number,))
        print(db_cursor.rowcount, "rows have been fetched.")
        account = db_cursor.fetchone()
        db_cursor.close()
    except Error as error:
        print("Error fetching row:", error)
    finally:
        bank_transaction.close(connection)

    return account


def fetch_all():
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    insert_sql = "select * from account"
    accounts = None

    try:
        db_cursor.execute(insert_sql)
        accounts = db_cursor.fetchall()
        print(db_cursor.rowcount, "rows have been fetched successfully")
        db_cursor.close()
    except Error as error:
        print("Error fetching rows:", error)
    finally:
        bank_transaction.close(connection)

    return accounts


def update(updated_account_dict):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    update_sql = "update account set account_number = %s, customer_id = %s, account_opening_date = %s, account_type = %s, " \
                 "account_status = %s where account_number = %s"

    updated_account_details = (
        updated_account_dict['account_number'],
        updated_account_dict['customer_id'],
        updated_account_dict['account_opening_date'],
        updated_account_dict['account_type'],
        updated_account_dict['account_status'],
        updated_account_dict['account_number']
    )

    try:
        db_cursor.execute(update_sql, updated_account_details)
        connection.commit()
        print(db_cursor.rowcount, "row has been updated successfully")
        db_cursor.close()
    except Error as error:
        print("Error updating row:", error)
    finally:
        bank_transaction.close(connection)


def delete_one_with_account_number(account_number):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    select_sql = "delete from account where account_number = %s"

    try:
        db_cursor.execute(select_sql, (account_number,))
        connection.commit()
        print(db_cursor.rowcount, "rows have been deleted.")
        db_cursor.close()
    except Error as error:
        print("Error deleting row:", error)
    finally:
        bank_transaction.close(connection)
