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
    
    print("\n--Quarter 1 Hours--")
    cursor.execute("SELECT emp_id, CONCAT(emp_first_name, ' ', emp_last_name), curr_quarter, SUM(emp_hours) "
                   "FROM Employees INNER JOIN EmployeeHours ON Employees.employee_id = EmployeeHours.emp_id "
                   "WHERE curr_quarter = 'Q1' "
                   "GROUP BY curr_quarter, emp_id "
                   "ORDER BY emp_id")
    list = cursor.fetchall()
    for e in list:
        print("Employee ID: {}\nEmployee Name: {}\nQuarter: {}\
                \nTotal Hours: {}\n".format(e[0],e[1],e[2], e[3]))
        
    print("\n--Quarter 2 Hours--")
    cursor.execute("SELECT emp_id, CONCAT(emp_first_name, ' ', emp_last_name), curr_quarter, SUM(emp_hours) "
                   "FROM Employees INNER JOIN EmployeeHours ON Employees.employee_id = EmployeeHours.emp_id "
                   "WHERE curr_quarter = 'Q2' "
                   "GROUP BY curr_quarter, emp_id "
                   "ORDER BY emp_id")
    list = cursor.fetchall()
    for e in list:
        print("Employee ID: {}\nEmployee Name: {}\nQuarter: {}\
                \nTotal Hours: {}\n".format(e[0],e[1],e[2], e[3]))
        
    print("\n--Quarter 3 Hours--")
    cursor.execute("SELECT emp_id, CONCAT(emp_first_name, ' ', emp_last_name), curr_quarter, SUM(emp_hours) "
                   "FROM Employees INNER JOIN EmployeeHours ON Employees.employee_id = EmployeeHours.emp_id "
                   "WHERE curr_quarter = 'Q3' "
                   "GROUP BY curr_quarter, emp_id "
                   "ORDER BY emp_id")
    list = cursor.fetchall()
    for e in list:
        print("Employee ID: {}\nEmployee Name: {}\nQuarter: {}\
                \nTotal Hours: {}\n".format(e[0],e[1],e[2], e[3]))
        
    print("\n--Quarter 4 Hours--")
    cursor.execute("SELECT emp_id, CONCAT(emp_first_name, ' ', emp_last_name), curr_quarter, SUM(emp_hours) "
                   "FROM Employees INNER JOIN EmployeeHours ON Employees.employee_id = EmployeeHours.emp_id "
                   "WHERE curr_quarter = 'Q4' "
                   "GROUP BY curr_quarter, emp_id "
                   "ORDER BY emp_id")
    list = cursor.fetchall()
    for e in list:
        print("Employee ID: {}\nEmployee Name: {}\nQuarter: {}\
                \nTotal Hours: {}\n".format(e[0],e[1],e[2], e[3]))

    db.close()
