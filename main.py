import mysql.connector
import getpass
# Establish a connection to the database
db = mysql.connector.connect(
host='localhost',
user='root',
password=getpass.getpass("Enter your MySQL password: "),
database='Ecommerce_delivery_db'
)
# Create a cursor object
obj = db.cursor()
# Functions for Product Management
def add_product():
name = input("Enter Product Name: ")
description = input("Enter Product Description: ")
price = float(input("Enter Product Price: "))
quantity_in_stock = int(input("Enter Quantity in Stock: "))
category = input("Enter Product Category: ")
sql = "INSERT INTO Product (name, description, price,
quantity_in_stock, category) VALUES (%s, %s, %s, %s, %s)"
val = (name, description, price, quantity_in_stock, category)
obj.execute(sql, val)
db.commit()
print("Product added successfully.")
def update_product():
product_id = int(input("Enter Product ID to update: "))
name = input("Enter new Product Name: ")
description = input("Enter new Product Description: ")
price = float(input("Enter new Product Price: "))
quantity_in_stock = int(input("Enter new Quantity in Stock: "))
category = input("Enter new Product Category: ")
sql = "UPDATE Product SET name = %s, description = %s, price = %s,
quantity_in_stock = %s, category = %s WHERE product_id = %s"
val = (name, description, price, quantity_in_stock, category, product_id)
obj.execute(sql, val)
db.commit()
print("Product updated successfully.")
def delete_product():
product_id = int(input("Enter Product ID to delete: "))
sql = "DELETE FROM Product WHERE product_id = %s"
val = (product_id,)
obj.execute(sql, val)
db.commit()
print("Product deleted successfully.")
def view_products():
sql = "SELECT * FROM Product"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Customer Management
def add_customer():
name = input("Enter Customer Name: ")
contact_information = input("Enter Contact Information: ")
shipping_address = input("Enter Shipping Address: ")
payment_details = input("Enter Payment Details: ")
sql = "INSERT INTO Customer (name, contact_information,
shipping_address, payment_details) VALUES (%s, %s, %s, %s)"
val = (name, contact_information, shipping_address, payment_details)
obj.execute(sql, val)
db.commit()
print("Customer added successfully.")
def update_customer():
customer_id = int(input("Enter Customer ID to update: "))
name = input("Enter new Customer Name: ")
contact_information = input("Enter new Contact Information: ")
shipping_address = input("Enter new Shipping Address: ")
payment_details = input("Enter new Payment Details: ")
sql = "UPDATE Customer SET name = %s, contact_information = %s,
shipping_address = %s, payment_details = %s WHERE customer_id = %s"
val = (name, contact_information, shipping_address, payment_details,
customer_id)
obj.execute(sql, val)
db.commit()
print("Customer updated successfully.")
def view_customers():
sql = "SELECT * FROM Customer"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Order Management
def place_order():
customer_id = int(input("Enter Customer ID: "))
order_status = input("Enter Order Status: ")
sql = "INSERT INTO `Order` (customer_id, order_date, order_status)
VALUES (%s, CURDATE(), %s)"
val = (customer_id, order_status)
obj.execute(sql, val)
db.commit()
print("Order placed successfully.")
def update_order_status():
order_id = int(input("Enter Order ID to update: "))
order_status = input("Enter new Order Status: ")
sql = "UPDATE `Order` SET order_status = %s WHERE order_id = %s"
val = (order_status, order_id)
obj.execute(sql, val)
db.commit()
print("Order status updated successfully.")
def view_orders():
sql = "SELECT * FROM `Order`"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Order Items Management
def add_order_item():
order_id = int(input("Enter Order ID: "))
product_id = int(input("Enter Product ID: "))
quantity = int(input("Enter Quantity: "))
total_price = float(input("Enter Total Price: "))
sql = "INSERT INTO OrderItems (order_id, product_id, quantity,
total_price) VALUES (%s, %s, %s, %s)"
val = (order_id, product_id, quantity, total_price)
obj.execute(sql, val)
db.commit()
print("Order item added successfully.")
def view_order_items():
sql = "SELECT * FROM OrderItems"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Delivery Management
def update_delivery_status():
delivery_id = int(input("Enter Delivery ID to update: "))
delivery_status = input("Enter new Delivery Status: ")
sql = "UPDATE Delivery SET delivery_status = %s WHERE delivery_id
= %s"
val = (delivery_status, delivery_id)
obj.execute(sql, val)
db.commit()
print("Delivery status updated successfully.")
def view_deliveries():
sql = "SELECT * FROM Delivery"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Payment Processing
def record_payment():
order_id = int(input("Enter Order ID: "))
payment_method = input("Enter Payment Method: ")
transaction_amount = float(input("Enter Transaction Amount: "))
sql = "INSERT INTO Payment (order_id, payment_date, payment_method,
transaction_amount) VALUES (%s, CURDATE(), %s, %s)"
val = (order_id, payment_method, transaction_amount)
obj.execute(sql, val)
db.commit()
print("Payment recorded successfully.")
def view_payments():
sql = "SELECT * FROM Payment"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for User Management
def add_user():
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
role = input("Enter Role (customer/admin): ")
sql = "INSERT INTO `User` (username, password, role) VALUES (%s,
%s, %s)"
val = (username, password, role)
obj.execute(sql, val)
db.commit()
print("User added successfully.")
def view_users():
sql = "SELECT * FROM `User`"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Review and Rating System
def add_review():
product_id = int(input("Enter Product ID: "))
customer_id = int(input("Enter Customer ID: "))
rating = int(input("Enter Rating (1-5): "))
comments = input("Enter Comments: ")
sql = "INSERT INTO ReviewsAndRatings (product_id, customer_id,
rating, comments) VALUES (%s, %s, %s, %s)"
val = (product_id, customer_id, rating, comments)
obj.execute(sql, val)
db.commit()
print("Review added successfully.")
def view_reviews():
sql = "SELECT * FROM ReviewsAndRatings"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Inventory Management
def update_inventory():
product_id = int(input("Enter Product ID: "))
quantity_in_stock = int(input("Enter Quantity in Stock: "))
reorder_point = int(input("Enter Reorder Point: "))
supplier_id = int(input("Enter Supplier ID: "))
sql = "UPDATE Inventory SET quantity_in_stock = %s, reorder_point =
%s, supplier_id = %s WHERE product_id = %s"
val = (quantity_in_stock, reorder_point, supplier_id, product_id)
obj.execute(sql, val)
db.commit()
print("Inventory updated successfully.")
def view_inventory():
sql = "SELECT * FROM Inventory"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Functions for Supplier Management
def add_supplier():
name = input("Enter Supplier Name: ")
contact_details = input("Enter Contact Details: ")
product_catalog = input("Enter Product Catalog: ")
sql = "INSERT INTO Supplier (name, contact_details, product_catalog)
VALUES (%s, %s, %s)"
val = (name, contact_details, product_catalog)
obj.execute(sql, val)
db.commit()
print("Supplier added successfully.")
def view_suppliers():
sql = "SELECT * FROM Supplier"
obj.execute(sql)
results = obj.fetchall()
for row in results:
print(row)
# Main menu
def main_menu():
while True:
print("\n--- Main Menu ---")
print("1. Manage Products")
print("2. Manage Customers")
print("3. Manage Orders")
print("4. Manage Order Items”)
