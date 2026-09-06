import mysql.connector

# Connect to server
cnx = mysql.connector.connect(host="127.0.0.1", port=3307, user="root", password="root")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SHOW DATABASES;")
print(list(cur))

# Close connection
cnx.close()
