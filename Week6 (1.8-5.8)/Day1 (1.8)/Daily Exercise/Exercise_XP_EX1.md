--------Run these first parts (lines 1-31) exactly once- lines 4-12 to create the Database
--------lines 12-34 to create the 2 tables and insert all the data into them
--------lines 35-41 will (when commented in) run each of the desired search/retrieve commands individually
-- CREATE DATABASE public
--     WITH 
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Israel.1252'
--     LC_CTYPE = 'English_Israel.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- CREATE TABLE items(
--  item_name VARCHAR (50) PRIMARY KEY,
--  price SMALLINT NOT NULL
-- );

-- CREATE TABLE customers(
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (50) NOT NULL
-- );

-- INSERT INTO items (item_name, price)
-- VALUES('Small Desk', 100),
-- ('Large desk', 300),
-- (' Fan', 80);

INSERT INTO customers (first_name, last_name)
-- VALUES('Greg','Jones'),
-- ('Sandra','Jones'),
-- ('Scott','Scott'),
-- ('Trevor','Green'),
-- ('Melanie','Johnson');

-- SELECT * FROM items;
-- SELECT * FROM items WHERE price>80;
-- SELECT * FROM items WHERE price<=300;
-- SELECT * FROM customers WHERE last_name=' Smith';
-- SELECT * FROM customers WHERE last_name=' Jones';
-- SELECT * FROM customers WHERE last_name != ' Scott';

