import psycopg2 as psy

host = "127.0.0.1"
user = "postgres"
password = "Schedule20"
db_name = "tg_bot"

# create blank variables just for no errors in auto detection errors
connection = ""
cursor = ""

try:
    # connect to an existing database
    connection = psy.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

# the cursor for performing database operation
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

# creating a new table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """ CREATE TABLE users(
#             id serial PRIMARY KEY,
#             first_name varchar(50) NOT NULL,
#             nick_name varchar(50) NOT NULL);"""
#         )
#         print("[INFO] Table created successfully")

# inserting new data into an existing table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """ INSERT INTO users (first_name, nick_name) VALUES
#             ('Oleg', 'Barracuda'),
#             ('Maria', 'Sunflower'),
#             ('Ivan', 'Tiger');"""
#         )
#         print("[INFO] Data was successfully inserted")

# printing data from an existing table
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
        )
        print(cursor.fetchone())


# getting column names from table
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_name = (cursor.fetchall()[0])[0]  # получаю имя таблицы в базе
        query = "SELECT column_name FROM information_schema.columns WHERE table_name = '" + table_name + "'"
        cursor.execute(query)
        column_names = [row[0] for row in cursor.fetchall()]  # получаю список столбцов
        print("column_names: ", column_names)

        # getting number of rows
        cursor.execute("SELECT COUNT(*) FROM " + table_name)
        print("Count = ", cursor.fetchone()[0])
        cursor.execute("SELECT * FROM " + table_name)
        print("all: ", cursor.fetchall())

# deleting an existing table
#     with connection.cursor() as cursor:
#         cursor.execute(
#             """DROP TABLE users;"""
#         )
#         print("[INFO] Table deleted successfully!")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
