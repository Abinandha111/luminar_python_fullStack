\-- =============================================================================
\-- MYSQL PRACTICE ASSESSMENT: SINGLE TABLE (QUESTIONS ONLY)
\-- =============================================================================

# /\*

# DATABASE & TABLE SCHEMA DETAILS

DATABASE NAME: ecommerce_db

TABLE NAME: products

## FIELD NAME     | DATA TYPE        | CONSTRAINTS / ATTRIBUTES

product_id     | INT              | PRIMARY KEY, AUTO_INCREMENT
product_name   | VARCHAR(150)     | NOT NULL, UNIQUE
category       | ENUM             | ('Electronics', 'Clothing', 'Books', 'Home')
price          | DECIMAL(10, 2)   | NOT NULL, DEFAULT 0.00
rating         | FLOAT            | NULL allowed
stock_quantity | INT              | NOT NULL, DEFAULT 0
is_available   | BOOLEAN          | DEFAULT TRUE
added_date     | DATE             | NOT NULL
last_restocked | DATETIME         | NULL allowed

# ================================================================================
PRACTICE QUESTIONS

\*/

\-- SECTION 1: DATABASE OPERATIONS

\-- QUESTION 1:
\-- Write a MySQL query to create a new database named `ecommerce_db`.

\-- QUESTION 2:
\-- Write a MySQL query to list all existing databases on the server.

\-- QUESTION 3:
\-- Write the statement to switch to and select `ecommerce_db` as the active database.

\-- SECTION 2: TABLE CREATION & CONSTRAINTS

\-- QUESTION 4:
\-- Write a query to create the `products` table with all specified fields,
-- proper data types (INT, VARCHAR, ENUM, DECIMAL, FLOAT, BOOLEAN, DATE, DATETIME),
-- and constraints (PRIMARY KEY, AUTO_INCREMENT, NOT NULL, UNIQUE, DEFAULT).

\-- SECTION 3: DATA INSERTION

\-- QUESTION 5:
\-- Write an INSERT query to add a single product with the following details:
\--   - product_name: 'Wireless Headphones'
\--   - category: 'Electronics'
\--   - price: 89.99
\--   - rating: 4.5
\--   - stock_quantity: 50
\--   - is_available: TRUE
\--   - added_date: '2024-01-10'
\--   - last_restocked: '2024-02-01 10:30:00'

\-- QUESTION 6:
\-- Write an INSERT query to insert multiple product records into the `products`
-- table in a single statement.

\-- SECTION 4: DATA RETRIEVAL (SELECT, OPERATORS, & KEYWORDS)

\-- QUESTION 7:
\-- Write a query to retrieve all columns and all records from the `products` table.

\-- QUESTION 8:
\-- Write a query to select a single record from `products` where `product_id` is 2.

\-- QUESTION 9 (Relational Operators):
\-- Write a query to select `product_name`, `price`, and `stock_quantity` for products
-- where `price` is greater than or equal to 50.00 AND `stock_quantity` is less than 20.

\-- QUESTION 10 (Logical Operators):
\-- Write a query to fetch all products that belong to category 'Electronics' OR 'Home',
\-- AND are currently available (`is_available` is TRUE).

\-- QUESTION 11 (Logical NOT & Relational !=):
\-- Write a query to find all products where `category` is NOT 'Books' and `price` is NOT equal to 0.00.

\-- QUESTION 12 (BETWEEN):
\-- Write a query to select products whose `price` falls BETWEEN 15.00 and 100.00.

\-- QUESTION 13 (IN Operator):
\-- Write a query using the `IN` operator to select products categorized under 'Electronics', 'Books', or 'Clothing'.

\-- QUESTION 14 (LIMIT & OFFSET):
\-- Write a query to retrieve 5 products from the table, skipping the first 3 records.

\-- SECTION 5: DATA MODIFICATION & DELETION

\-- QUESTION 15 (UPDATE Single Record):
\-- Write a query to update the product with `product_id = 3`, changing its `price`
-- to 45.50 and setting `last_restocked` to current date and time.

\-- QUESTION 16 (UPDATE Multiple Records):
\-- Write a query to update `is_available` to FALSE for all products where
-- `stock_quantity` is equal to 0.

\-- QUESTION 17 (DELETE Single Record):
\-- Write a query to delete a product where `product_id` is 5.

\-- QUESTION 18 (DELETE Conditional):
\-- Write a query to delete all products where `added_date` is before '2022-01-01'
-- and `stock_quantity` is 0.