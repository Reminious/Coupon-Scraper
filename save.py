import mysql.connector
import pandas as pd

file_path = 'C:\\Users\\XX\\Desktop\\scrapy\\links.csv'
df = pd.read_csv(file_path)
host = "localhost"
user = "root"
passwd = "123123"
database = "testdb"

try:
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
    if connection.is_connected():
        db_info=connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        for i, row in df.iterrows():
            url = df.iloc[i]['URL']
            shop_name = df.iloc[i]['Shop Name']
            cursor.execute("INSERT INTO website (url, shop_name) VALUES (%s, %s)", (url, shop_name))
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into website table")
except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
