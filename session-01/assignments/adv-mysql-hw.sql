-- Abel Limas 
-- Adv. MySQL Assignment
-- 5/21/21 

-- 1. Run the script to create Northwind db MySQL_Northwind.sql
USE northwind; -- MySQL_Northwind.sql was executed inside it's own file.

-- 2. Display the names and job titles (ContactTitle) of contacts who are also owners. [Use the Customers table]
SELECT first_name, job_title FROM customers WHERE job_title = 'Owner';

-- 3. Display the names and prices of those products with prices of $50 or more. [Use the Products table]
SELECT product_name, list_price FROM products WHERE list_price > 50;

-- 4. Display the names and prices of those products with prices greater than or equal to $15 but less than or equal to $20. [Use the Products table]
SELECT product_name, list_price FROM products WHERE list_price >= 15 AND list_price <= 20;

-- 5. Display the shipping fee total. [Use the Products table] Use Group By
SELECT shipping_fee FROM products;


-- 6. Display the 05-04-2006 shipping fee total. [Use the Orders table] Use Group By
SELECT shipping_fee, shipped_date from orders WHERE shipped_date = '2006-05-04 00:00:00' GROUP BY shipping_fee ORDER BY shipping_fee;


-- 7.  Display the names of ALL suppliers and name of their products. [ Use the Products and Suppliers tables] Using Joins
SELECT suppliers.id, suppliers.company, products.product_name
FROM suppliers
CROSS JOIN products
ORDER BY suppliers.id;

-- 8. Display all the suppliers that have purchase order quantity more than 40. Using Joins
SELECT suppliers.id, suppliers.company, products.product_name, products.reorder_level
FROM suppliers
CROSS JOIN products
WHERE products.reorder_level > 40;

--
-- STORED PROCEDURE

-- Create employee and employee Log table which contain all the rows with operation (insert/update/delete) performed on rows
Create Table EmpDemo
(
EmpNoint Int Primary Key, 
Ename Varchar(15),
Salary Float,
DeptNo Int
);

Create Table EmpDemo_Log (
EmpNoint Int, 
Ename Varchar(15), 
Salary Float,
DeptNo Int,
-- Act varchar(15), 
DateCreated DateTime
);


--
-- 9. Create a trigger for EmpDemo table so that when a record is inserted/updated and deleted it get inserted into the EmpDemo_Log table

CREATE TRIGGER EmpLogInsertTrigger
    AFTER INSERT ON EmpDemo
    FOR EACH ROW
INSERT INTO EmpDemo_log
SET action = 'insert',
    EmpNoint = NEW.EmpNoint,
    Ename = NEW.Ename,
    Salary = NEW.Salary,
    DeptNo = NEW.DeptNo,
    DateCreated = NOW();


CREATE TRIGGER EmpLogTrigger
    AFTER UPDATE ON EmpDemo
    FOR EACH ROW
INSERT INTO EmpDemo_log
SET action = 'update',
    EmpNoint = OLD.EmpNoint,
    Ename = OLD.Ename,
    Salary = OLD.Salary,
    DeptNo = OLD.DeptNo,
    DateCreated = NOW();
    
    
CREATE TRIGGER EmpLogDeleteTrigger
    AFTER DELETE ON EmpDemo
    FOR EACH ROW
INSERT INTO EmpDemo_log
SET action = 'delete',
    EmpNoint = OLD.EmpNoint,
    Ename = OLD.Ename,
    Salary = OLD.Salary,
    DeptNo = OLD.DeptNo,
    DateCreated = NOW();
    

SELECT * FROM EmpDemo_Log;

INSERT INTO EmpDemo VALUES (1, 'TEST3', 50000.00, 1);

SELECT * FROM EmpDemo_Log;


-- 10. Write a procedure to get employee data based on DeptNo. If value for DeptNo is not given get all employees (using Optional parameter)
-- DELIMITER // 
-- CREATE PROCEDURE get_emp_data
-- BEGIN 
-- select * FROM EmpDemo
-- END //
-- DELIMITER;


-- 11. Write a procedure to insert data into EmpDemo table and get new EmpNo generated as Output parameter (use transaction and error handling)



-- 12. Create a view for EmpDemo table and try to Insert records into the view.
CREATE VIEW emp_view 
AS
SELECT * FROM EmpDemo;


INSERT INTO emp_view
VALUES (007, 'TEST1', 50000.00, 4);

INSERT INTO emp_view
VALUES (001, 'TEST3', 50000.00, 4);

SELECT * FROM EmpDemo;

