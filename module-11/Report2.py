import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "milkshakes",
    "host": "127.0.0.1",
    "database": "BacchusWinery",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)
finally:
    cursor = db.cursor()

try:
    cursor.execute("SELECT w.wine_name, COUNT(s.sale_id) AS total_sales "
                   "FROM Wine w LEFT JOIN Sales s ON w.wine_id = s.wine_id "
                   "GROUP BY w.wine_name")
    all_wines_data = cursor.fetchall()
    print("Wines selling status:")
    for wine, total_sales in all_wines_data:
        print(f"{wine}: {'Yes' if total_sales else 'No'}")

    cursor.execute("SELECT w.wine_name "
                   "FROM Wine w LEFT JOIN Sales s ON w.wine_id = s.wine_id "
                   "GROUP BY w.wine_name HAVING COUNT(s.sale_id) = 0")
    unsold_wines = cursor.fetchall()
    if unsold_wines:
        print("\nUnsold wines:")
        for wine in unsold_wines:
            print(wine[0])
    else:
        print("\nUnsold wines: 0")

    cursor.execute("SELECT wine_id, distributor_name "
                   "FROM WineDistributor wd "
                   "JOIN Distributor d ON wd.distributor_id = d.distributor_id "
                   "ORDER BY wd.wine_id, d.distributor_id")
    wine_distributor_data = cursor.fetchall()
    print("\nDistributor information for each wine:")
    current_wine = None
    for wine_id, distributor_name in wine_distributor_data:
        if wine_id != current_wine:
            print(f"\nWine ID: {wine_id}")
            current_wine = wine_id
        print(f"- {distributor_name}")

except mysql.connector.Error as error:
    print("Error querying the database:", error)

cursor.close()

db.close()
