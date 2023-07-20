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
    with connection.cursor() as cursor:
        cursor.execute(
            """ INSERT INTO users (first_name, nick_name) VALUES
            ('Oleg', 'Barracuda');"""
        )
        print("[INFO] Data was successfully inserted")

# printing data from an existing table
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
        )
        print(cursor.fetchone())

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
