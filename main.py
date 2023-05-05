import mysql.connector

# Установка соединения с базой данных
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Создание курсора для работы с базой данных
mycursor = mydb.cursor()

# Создание таблицы "product"
mycursor.execute("CREATE TABLE product (id INT PRIMARY KEY, "
                 "name VARCHAR(255), description TEXT, "
                 "price DECIMAL(10,2), category_id INT, "
                 "manufacturer_id INT, "
                 "FOREIGN KEY (category_id) REFERENCES category(id), "
                 "FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id))")

# Создание таблицы "category"
mycursor.execute("CREATE TABLE category (id INT PRIMARY KEY, "
                 "name VARCHAR(255))")

# Создание таблицы "manufacturer"
mycursor.execute("CREATE TABLE manufacturer (id INT PRIMARY KEY, "
                 "name VARCHAR(255))")

# Создание таблицы "order"
mycursor.execute("CREATE TABLE order (id INT PRIMARY KEY, "
                 "client_id INT, "
                 "status VARCHAR(255), "
                 "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "
                 "FOREIGN KEY (client_id) REFERENCES client(id))")

# Создание таблицы "client"
mycursor.execute("CREATE TABLE client (id INT PRIMARY KEY, name VARCHAR(255), "
                 "email VARCHAR(255), "
                 "phone VARCHAR(255), "
                 "address VARCHAR(255))")

# Создание таблицы "cart"
mycursor.execute("CREATE TABLE cart (id INT PRIMARY KEY, "
                 "product_id INT, "
                 "order_id INT, "
                 "quantity INT, "
                 "FOREIGN KEY (product_id) REFERENCES product(id), "
                 "FOREIGN KEY (order_id) REFERENCES order(id))")
