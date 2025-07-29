import mysql.connector as sql
conn=sql.connect(user='root',passwd='jerin@330077',database='marketing_system_and_sales_system')
if conn.is_connected():
    print('successfully connected')

c1=conn.cursor()

c1.execute('create table customer_details(customer_name varchar(50) primary key,product_name varchar(60))')
print('Table Created')

c1.execute('create table products_brand(customer_name varchar(50),product_type varchar(40),product_brand varchar(50), products_available int(9))')
print('Table Created')
               
c1.execute('create table order_placement(customer_name varchar(50),product_name varchar(50),demanding_quantity int(9))')
print('Table Created')

c1.execute('create table order_details(customer_name varchar(50),mobile_number int(10),address varchar(999), date_to_deliver DATE)')
print('Table Created')

c1.execute('create table cancellation_of_order(customer_name varchar(50), order_number int(15), products_contained varchar(90),reason_for_cancelling varchar(50),confirm_cancellation varchar(20))')
print('Table Created')

