import csv
import mysql.connector

conn = mysql.connector.connect(
    user='root',
    password='1111',
    host='127.0.0.1',
    database='dev_train',
    auth_plugin='mysql_native_password')

cur = conn.cursor()

# file = open('students.csv')
file = open('customer.csv')
csv_data = csv.reader(file)

cur.execute('DROP TABLE IF EXISTS customers')

sql_create = '''CREATE TABLE customers (
        customers_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        customer_id VARCHAR(100),
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        company_name VARCHAR(100),
        billing_address1 VARCHAR(100),
        billing_address2 VARCHAR(100),
        city VARCHAR(100),
        state VARCHAR(100),
        postal_code VARCHAR(100),
        country VARCHAR(100),
        phone_number VARCHAR(100),
        email_address VARCHAR(100),
        created_date VARCHAR(100)
    )'''
cur.execute(sql_create)

skipHeader = True
for row in csv_data:
    if skipHeader:
        skipHeader = False
        continue

    sql_insert = '''INSERT INTO customers(customer_id, first_name, last_name, company_name, billing_address1, billing_address2, city, state,
                      postal_code, country, phone_number, email_address, created_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.execute(sql_insert, row)

conn.commit()

conn.close()
