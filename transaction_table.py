import bank_transaction
from mysql.connector import Error


def create_transaction_details_table():
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    sql_create_transaction_details = "CREATE TABLE if not exists transaction_details (" \
                                     "transaction_id INTEGER NOT NULL," \
                                     "account_number INTEGER NOT NULL," \
                                     "transaction_date DATE," \
                                     "transaction_type VARCHAR(30) NOT NULL," \
                                     "transaction_amount VARCHAR(20) NOT NULL," \
                                     "transaction_medium INTEGER NOT NULL," \
                                     "CONSTRAINT transaction_details_pk PRIMARY KEY(transaction_number)," \
                                     "CONSTRAINT transaction_details_fk FOREIGN KEY(account_number) REFERENCES account(account_number))"

    try:
        db_cursor.execute(sql_create_transaction_details)
        connection.commit()
        print("Your transaction_details table is created")
        db_cursor.close()
    except Error as error:
        print("Error creating transaction_details table", error)
    finally:
        bank_transaction.close(connection)


def insert(new_transaction_dict):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    insert
    sql_create_transaction_details = "insert into transaction_details (account_number, transaction_date, transaction_type, transaction_amount, transaction_medium)" \
                                     "values (%s, %s, %s, %s, %s)"

    transaction_details = (
        new_transaction_dict['account_number'],
        new_transaction_dict['transaction_date'],
        new_transaction_dict['transaction_type'],
        new_transaction_dict['transaction_amount'],
        new_transaction_dict['transaction_medium']
    )


try:
    db_cursor.execute(insert_sql_create_transaction_details)
    connection.commit()
    print(db_cursor.rowcount, "the row has been inserted successfully")
    db_cursor.close()
except Error as error:
    print("Error inserting row:", error)
finally:
    bank_transaction.close(connection)


def fetch_all():
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    insert_sql_create_transaction_details = "select * from transaction_details;"
    transactions = None

    try:
        db_cursor.execute(insert_sql_create_transaction_details)
        transactions = db_cursor.fetchall()
        print(db_cursor.rowcount, "the row has been fetched successfully")
        db_cursor.close()
    except Error as error:
        print("Error fetching rows:", error)
    finally:
        bank_transaction.close(connection)

        return transactions


def fetch_one_with_transaction_id(transaction_id):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    select_sql_create_transaction_details = "select * from account where transaction_id = %d;", transaction_id
    transaction = None

    try:
        db_cursor.execute(select_sql_create_transaction_details, (transaction_id,))
        print(db_cursor.rowcount, "rows fetched")
        transaction = db_cursor.fetchone()
        db_cursor.close()
    except Error as error:
        print("Error fetching row:", error)
    finally:
        bank_transaction.close(connection)

    return transaction


def update(updated_transaction_dict);


connection = bank_transaction.connect()
db_cursor = connection.cursor()

update_sql_create_transaction_details = "update transaction_detail set (account_number = %s, transaction_date = %s, transaction_type = %s, " \
                                        "transaction_amount = %s, account_status = %s) where transaction_id = %d", \

updated_transaction_details = (
    updated_transaction_dict['account_number'],
    updated_transaction_dict['transaction_date'],
    updated_transaction_dict['transaction_type'],
    updated_transaction_dict['transaction_amount'],
    updated_transaction_dict['account_status']
    updated_transaction_dict['transaction_id']
    )

try:
    db_cursor.execute(select_sql_create_transaction_details, updated_transaction_details)
    connection.commit()
    print(db_cursor.rowcount, "rows updated successfully")
    db_cursor.close()
except Error as error:
    print("Error uddating row:", error)
finally:
    bank_transaction.close(connection)


def delete_one_with_transaction_id(transaction_id):
    connection = bank_transaction.connect()
    db_cursor = connection.cursor()

    select_sql_create_transaction_details = "delete from transaction_details where transaction_id = %s"

    try:
        db_cursor.execute(select_sql_create_transaction_details, (transaction_id,))
        connection.commit()
        print(db_cursor.rowcount, "rows have been deleted")
        db_cursor.close()
    except Error as error:
        print("Error deleting row:", error)
    finally:
        bank_transaction.close(connection)
