from bank_transaction import *
from mysql.connector import Error


def create_table():
    connection = connect()
    db_cursor = connection.cursor()

    create_sql= "CREATE TABLE if not exists customer (" \
                "customer_id INTEGER NOT NULL auto_increment," \
                "first_name VARCHAR (30) NOT NULL," \
                "last_name VARCHAR(30) NOT NULL," \
                "middle_name VARCHAR(30) NOT NULL," \
                "mobile_number VARCHAR(10) NOT NULL," \
                "occupation VARCHAR(10) NOT NULL," \
                "date_of_birth DATE," \
                "CONSTRAINT customer_pk PRIMARY KEY(customer_id)" \
                ")"
    try:
        db_cursor.execute(create_sql)
        connection.commit()
        print("Your customer table has been created")
        db_cursor.close()
    except Error as error:
        print("Error creating customer table", error)
    finally:
        close(connection)


def insert(new_customer_dict):
    connection = connect()
    db_cursor = connection.cursor()

    insert_sql = "insert into customer (first_name, last_name, middle_name, mobile_number, occupation, date_of_birth) " \
                 "values (%s, %s, %s, %s, %s, %s)"

    customer_details = (
        new_customer_dict['first_name'],
        new_customer_dict['last_name'],
        new_customer_dict['middle_name'],
        new_customer_dict['mobile_number'],
        new_customer_dict['occupation'],
        new_customer_dict['date_of_birth']
    )

    try:
        db_cursor.execute(insert_sql, customer_details)
        connection.commit()
        print(db_cursor.rowcount, "row has been inserted")
        db_cursor.close()
    except Error as error:
        print("Error inserting new row:", error)
    finally:
        close(connection)


def fetch_all():
    connection = connect()
    db_cursor = connection.cursor()

    select_sql = "select * from customer"
    customers = None

    try:
        db_cursor.execute(select_sql)
        customers = db_cursor.fetchall()
        print(db_cursor.rowcount, "rows has been fetched")
        db_cursor.close()
    except Error as error:
        print("Error fetching rows:", error)
    finally:
        close(connection)

    return customers


def fetch_one_with_customer_id(customer_id):
    connection = connect()
    db_cursor = connection.cursor()

    select_sql = "select * from account where customer_id = %s"
    customer = None

    try:
        db_cursor.execute(select_sql, (customer_id,))
        print(db_cursor.rowcount, "rows have been fetched.")
        customer = db_cursor.fetchone()
        db_cursor.close()
    except Error as error:
        print("Error fetching row:", error)
    finally:
        close(connection)

    return customer


def update(updated_customer_dict):
    connection = connect()
    db_cursor = connection.cursor()
    update_sql = "update customer set first_name = %s, last_name = %s, middle_name = %s, mobile_number = %s, occupation = %s, date_of_birth = %s " \
                 "where customer_id = %s"

    updated_customer_details = (
        updated_customer_dict['first_name'],
        updated_customer_dict['last_name'],
        updated_customer_dict['middle_name'],
        updated_customer_dict['mobile_number'],
        updated_customer_dict['occupation'],
        updated_customer_dict['date_of_birth'],
        updated_customer_dict['customer_id']
    )

    try:
        db_cursor.execute(update_sql, updated_customer_details)
        connection.commit()
        print(db_cursor.rowcount, "row has been updated successfully")
        db_cursor.close()
    except Error as error:
        print("Error updating row:", error)
    finally:
        close(connection)


def delete_one_with_customer_id(customer_id):
    connection = connect()
    db_cursor = connection.cursor()

    select_sql = "delete from customer where customer_id = %s"

    try:
        db_cursor.execute(select_sql, (customer_id,))
        connection.commit()
        print(db_cursor.rowcount, "rows have been deleted.")
        db_cursor.close()
    except Error as error:
        print("Error deleting row:", error)
    finally:
        close(connection)
