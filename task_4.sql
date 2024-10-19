-- -- author: Anochili Blessing Ebele
-- -- purpose: Write a script that prints the full description of the table books from the database alx_book_store in your MySQL server. 
-- date: 14/10/2024

-- Get the full description of the 'books' table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books';
