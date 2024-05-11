CREATE DATABASE BacchusWinery;

USE BacchusWinery;

CREATE TABLE Departments (
    department_id VARCHAR(5),
    department_name VARCHAR(80),
    hours_worked VARCHAR(80),
    PRIMARY KEY (department_id)
);

INSERT INTO Departments
VALUES ('001', 'Owner', '60 hours/week'),
       ('900', 'Marketing', '60 hours/week'),
       ('901', 'Accounting/Payroll', '60 hours/week'),
       ('902', 'Human Resources', '60 hours/week'),
       ('903', 'Distribution', '60 hours/week'),
       ('700A', '1st Shift 1st Shift Wine Bottler', '40 hours/week'),
       ('700B', '2nd Shift 1st Shift Wine Bottler', '32 hours/week'),
       ('701A', '1st Shift 1st Shift Wine Maker', '45 hours/week'),
       ('701B', '2nd Shift 1st Shift Wine Maker', '45 hours/week'),
       ('702A', '1st Shift 1st Shift Wine Shipper', '40 hours/week'),
       ('702B', '2nd Shift 1st Shift Wine Shipper', '40 hours/week');

CREATE TABLE QuartersDates (
    quarter_id varchar(10),
    quarter_dates varchar(30),
    PRIMARY KEY (quarter_id)

);

INSERT INTO QuartersDates 
VALUES  ('1st','2023-07-05'),
        ('2nd','2023-10-03'),
        ('3rd','2024-01-01'),
        ('4th','2024-04-01');


CREATE TABLE Employees (
    employee_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    emp_first_name varchar(30),
    emp_last_name varchar(30),
    emp_title varchar(60),
    hire_date date,
    department_id varchar(4),
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

INSERT INTO Employees (emp_first_name, emp_last_name, emp_title, hire_date, department_id)
VALUES 
('Stan', 'Bacchus', 'Owner/Chief Executive Officer', '2020-06-23', '001'),
('Davis', 'Bacchus', 'Owner/Chief Executive Officer', '2020-06-23', '001'),
('Janet', 'Collins', 'Chief Financial Officer', '2012-01-18', '901'),
('Roz', 'Murphy', 'Chief Marketing Officer', '2003-11-02', '900'),
('Bob', 'Ulrich', 'Marketing Assistant', '2018-12-19', '900'),
('Henry', 'Doyle', 'Chief Operations Officer', '2004-07-25', '903'),
('Maria', 'Costanza', 'Distribution Manager', '2007-09-07', '903'),
('Tony', 'Stark','1st Shift Wine Bottler' ,'2010-01-15','700A'),
('Thor', 'Odinson', '1st Shift Wine Bottler','2011-02-10','700A'),
('Janet', 'Van Dyke','1st Shift Wine Bottler','2014-03-15','700A'),
('Hank', 'Pym','1st Shift 1st Shift Wine Bottler','2016-10-13','700A'),
('Bruce', 'Banner', '1st Shift Wine Bottler','2013-12-10','700A'),
('Steve','Rogers','2nd Shift Wine Bottler','2005-06-09','700B'),
('Clint','Barton','2nd Shift Wine Bottler','2015-03-05','700B'),
('Pietro','Frank','2nd Shift Wine Bottler','2014-08-25','700B'),
('Wanda','Frank','1st Shift Wine Maker','2009-06-02','701A'),
('Luke','Charles','1st Shift Wine Maker','2011-03-04','701A'),
('Victor','Shade','1st Shift Wine Maker','2010-05-13','701A'),
('Dane','Whitman','1st Shift Wine Maker','2008-07-15','701A'),
('Natasha','Romanoff','2nd Shift Wine Maker','2011-09-12','701B'),
('Philip','McCoy','2nd Shift Wine Maker','2018-07-05','701B'),
('Heather','Douglas','2nd Shift Wine Maker','2019-04-05','701B'),
('Patricia','Walker','1st Shift Wine Shipper','2017-11-07','702A'),
('Simon','Williams','1st Shift Wine Shipper','2020-01-12','702A'),
('Matt','Hawk','1st Shift Wine Shipper','2021-06-13','702A'),
('Carol','Danvers','2nd Shift Wine Shipper','2012-02-01','702B'),
('Peter','Parker','2nd Shift Wine Shipper','2018-05-10','702B');

CREATE TABLE EmployeeHours (
    entry_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    emp_id int,
    curr_quarter varchar(30),
    emp_hours int,
    FOREIGN KEY(emp_id) REFERENCES Employees(employee_id)
);

ALTER TABLE EmployeeHours AUTO_INCREMENT=100;

INSERT INTO EmployeeHours (emp_id, curr_quarter, emp_hours)
VALUES 
(1,'Q1', 501),
(1,'Q2', 548),
(1,'Q3', 623),
(1,'Q4', 559),
(2,'Q1', 515),
(2,'Q2', 510),
(2,'Q3', 520),
(2,'Q4', 544),
(3,'Q1', 528),
(3,'Q2', 555),
(3,'Q3', 612),
(3,'Q4', 624),
(4,'Q1', 225),
(4,'Q2', 283),
(4,'Q3', 270),
(4,'Q4', 304),
(5,'Q1', 488),
(5,'Q2', 622),
(5,'Q3', 687),
(5,'Q4', 612),
(6,'Q1', 490),
(6,'Q2', 476),
(6,'Q3', 598),
(6,'Q4', 708),
(7,'Q1', 483),
(7,'Q2', 498),
(7,'Q3', 601),
(7,'Q4', 723),
(001,'Q1',520),
(001,'Q2',510),
(001,'Q3',520),
(001,'Q4',530),
(002,'Q1',520),
(002,'Q2',520),
(002,'Q3',500),
(002,'Q4',530),
(003,'Q1',520),
(003,'Q2',520),
(003,'Q3',520),
(003,'Q4',540),
(004,'Q1',520),
(004,'Q2',520),
(004,'Q3',520),
(004,'Q4',520),
(005,'Q1',520),
(005,'Q2',560),
(005,'Q3',500),
(005,'Q4',560),
(006,'Q1',416),
(006,'Q2',500),
(006,'Q3',430),
(006,'Q4',480),
(007,'Q1',430),
(007,'Q2',450),
(007,'Q3',480),
(007,'Q4',500),
(008,'Q1',416),
(008,'Q2',416),
(008,'Q3',416),
(008,'Q4',416),
(009,'Q1',585),
(009,'Q2',600),
(009,'Q3',585),
(009,'Q4',585),
(010,'Q1',585),
(010,'Q2',585),
(010,'Q3',585),
(010,'Q4',585),
(011,'Q1',585),
(011,'Q2',585),
(011,'Q3',585),
(011,'Q4',585),
(012,'Q1',640),
(012,'Q2',585),
(012,'Q3',620),
(012,'Q4',585),
(013,'Q1',585),
(013,'Q2',585),
(013,'Q3',585),
(013,'Q4',585),
(014,'Q1',680),
(014,'Q2',585),
(014,'Q3',585),
(014,'Q4',600),
(015,'Q1',585),
(015,'Q2',585),
(015,'Q3',585),
(015,'Q4',585),
(016,'Q1',520),
(016,'Q2',560),
(016,'Q3',520),
(016,'Q4',520),
(017,'Q1',520),
(017,'Q2',520),
(017,'Q3',520),
(017,'Q4',520),
(018,'Q1',520),
(018,'Q2',520),
(018,'Q3',520),
(018,'Q4',520),
(019,'Q1',520),
(019,'Q2',520),
(019,'Q3',520),
(019,'Q4',520),
(020,'Q1',520),
(020,'Q2',520),
(020,'Q3',520),
(020,'Q4',520);






CREATE TABLE 1st Shift Wine (
    wine_id int NOT NULL AUTO_INCREMENT,
    wine_name varchar(30),
    wine_cost NOT NULL,
    PRIMARY KEY (wine_id)
);

ALTER TABLE 1st Shift Wine AUTO_INCREMENT=380;

INSERT INTO 1st Shift Wine(wine_name,wine_cost)
VALUES
('Merlot',28),
('Cabernet',22),
('Chablis',50),
('Chardonnay',15);





CREATE TABLE Sales (
    sale_id int NOT NULL AUTO_INCREMENT,
    wine_id int,
    sale_date date,
    PRIMARY KEY (sale_id),
    FOREIGN KEY (wine_id) REFERENCES 1st Shift Wine(wine_id)
);

ALTER TABLE Sales AUTO_INCREMENT=100;

INSERT INTO Sales(wine_id, sale_date)
VALUES
(380, '2024-03-01'),
(381, '2024-03-23'),
(382, '2024-04-01'),
(383, '2024-03-16'),
(383, '2024-03-02'),
(380, '2024-03-28')
(381, '2024-02-12');

CREATE TABLE WineInventory (
    wine_inventory_id int NOT NULL AUTO_INCREMENT,
    wine_id int,
    stock int,
    PRIMARY KEY (wine_inventory_id),
    FOREIGN KEY (wine_id) REFERENCES 1st Shift Wine(wine_id)
);

INSERT INTO WineInventory(wine_id, stock)
VALUES
(380, 982),
(381, 384),
(382, 492),
(383, 131);



CREATE TABLE SupplierInfo (
    supplier_id int NOT NULL AUTO_INCREMENT,
    supplier_name varchar(60),
    PRIMARY KEY (supplier_id)
);

INSERT INTO SupplierInfo(supplier_name)
VALUES
('Corks ''R'' Us'),
('UPS'),
('Vatsmore');





CREATE TABLE OrderTracking (
    tracking_number varchar(8) NOT NULL,
    expected_delivery date,
    actual_delivery date,
    PRIMARY KEY (tracking_number)
);

INSERT INTO OrderTracking
VALUES
('XY2362ZA', '2024-02-01', '2024-01-23'),
('XY3248ZB', '2024-02-01', '2024-01-28'),
('XY9835ZC', '2024-02-01', '2024-01-27'),
('XY6783ZD', '2024-03-01', '2024-02-22'),
('XY5728ZE', '2024-03-01', '2024-03-24'),
('XY4719ZF', '2024-03-01', '2024-03-18'),
('XY4723ZG', '2024-03-01', '2024-02-28'),
('XY4761ZH', '2024-04-01', '2024-03-30');







CREATE TABLE SupplierDelivery (
    delivery_id int NOT NULL AUTO_INCREMENT,
    supplier_id int,
    tracking_number varchar(8),
    PRIMARY KEY (delivery_id),
    FOREIGN KEY (supplier_id) REFERENCES SupplierInfo(supplier_id)
);

INSERT INTO SupplierDelivery(supplier_id, tracking_number)
VALUES
(3,'XY2362ZA'),
(1, 'XY3248ZB'),
(1, 'XY9835ZC'),
(2, 'XY6783ZD'),
(1, 'XY5728ZE'),
(2, 'XY4719ZF'),
(3, 'XY4723ZG'),
(1, 'XY4761ZH');




CREATE TABLE Supplies (
    supply_id int NOT NULL,
    supplier_id int,
    supply_name varchar(60),
    PRIMARY KEY (supply_id),
    FOREIGN KEY (supplier_id) REFERENCES SupplierInfo(supplier_id)
);

INSERT INTO Supplies
VALUES
(101, 1, 'Bottles'),
(102, 1, 'Corks'),
(201, 2, 'Labels'),
(202, 2, 'Boxes'),
(301, 3, 'Vats'),
(302, 3, 'Tubing');





CREATE TABLE Inventory (
    inventory_id varchar(2) NOT NULL,
    supply_id int,
    product_amount int,
    checked_date date,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (supply_id) REFERENCES Supplies(supply_id)
);


INSERT INTO Inventory
VALUES
('1A', 101, 500, '2024-04-01'),
('2A', 102, 550, '2024-04-01'),
('3A', 201, 60, '2024-04-03'),
('4A', 202, 75, '2024-03-29'),
('5A', 301, 4, '2024-04-15'),
('6A', 302, 7, '2024-04-28');



CREATE TABLE Distributor (
    distributor_id int AUTO_INCREMENT PRIMARY KEY,
    distributor_name varchar(60),
);

INSERT INTO Distributor(distributor_name)
VALUES
('Target'),
('Trader Joes'),
('Costco'),
('Walmart'),
('Tesco'),
('Sams');

CREATE TABLE WineDistributor(
    wine_id int NOT NULL,
    distributor_id int NOT NULL,
    PRIMARY KEY(wine_id, distributor_id)
);

INSERT INTO WineDistributor
VALUES
(380, 2),
(381, 2),
(383, 1),
(382, 1),
(380, 3),
(381, 3),
(382, 3);
