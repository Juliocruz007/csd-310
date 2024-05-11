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

    # Month of January
    print("\n--DISPLAYING Gap between expected delivery and actual delivery for JANUARY--")
    cursor.execute("SELECT supplier_id, OrderTracking.expected_delivery, OrderTracking.actual_delivery, DATEDIFF(OrderTracking.expected_delivery, OrderTracking.actual_delivery) AS DayDiff\
                   FROM SupplierDelivery\
                   INNER JOIN OrderTracking\
                   ON SupplierDelivery.tracking_number = OrderTracking.tracking_number\
                   WHERE Month(actual_delivery) = 1")
    list = cursor.fetchall()
    for e in list:
        print("supplier_id: {}\nexpected_delivery:{}\
                \nactual_delivery:{}\nDay Difference: {}\n".format(e[0],e[1],e[2], e[3]))

    # Month of February
    print("\n--DISPLAYING Gap between expected delivery and actual delivery for FEBRUARY--")
    cursor.execute("SELECT supplier_id, OrderTracking.expected_delivery, OrderTracking.actual_delivery, DATEDIFF(OrderTracking.expected_delivery, OrderTracking.actual_delivery) AS DayDiff\
                   FROM SupplierDelivery\
                   INNER JOIN OrderTracking\
                   ON SupplierDelivery.tracking_number = OrderTracking.tracking_number\
                   WHERE Month(actual_delivery) = 2")
    list = cursor.fetchall()
    for e in list:
        print("supplier_id: {}\nexpected_delivery:{}\
                \nactual_delivery:{}\nDay Difference: {}\n".format(e[0],e[1],e[2], e[3]))

    # Month of March
    print("\n--DISPLAYING Gap between expected delivery and actual delivery for MARCH--")
    cursor.execute("SELECT supplier_id, OrderTracking.expected_delivery, OrderTracking.actual_delivery, DATEDIFF(OrderTracking.expected_delivery, OrderTracking.actual_delivery) AS DayDiff\
                   FROM SupplierDelivery\
                   INNER JOIN OrderTracking\
                   ON SupplierDelivery.tracking_number = OrderTracking.tracking_number\
                   WHERE Month(actual_delivery) = 3")
    list = cursor.fetchall()
    for e in list:
        print("supplier_id: {}\nexpected_delivery:{}\
                \nactual_delivery:{}\nDay Difference: {}\n".format(e[0],e[1],e[2], e[3]))
    db.close()
