-- ===================================================================
-- BOOKSTORE DATABASE DESIGN
-- Relations and Tuples for Books, Customers, and Sales
-- ===================================================================

-- ===================================================================
-- 1. BOOKS RELATION
-- ===================================================================
CREATE TABLE Books (
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

-- Insert tuples into Books relation
INSERT INTO Books (Book_ID, Title, Author, Price) VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 12.99),
(2, '1984', 'George Orwell', 13.99),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 11.99),
(4, 'Pride and Prejudice', 'Jane Austen', 10.99),
(5, 'The Catcher in the Rye', 'J.D. Salinger', 14.99);

-- ===================================================================
-- 2. CUSTOMERS RELATION
-- ===================================================================
CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(15)
);

-- Insert tuples into Customers relation
INSERT INTO Customers (Customer_ID, Name, Email, Phone) VALUES
(101, 'John Smith', 'john.smith@email.com', '555-0101'),
(102, 'Sarah Johnson', 'sarah.johnson@email.com', '555-0102'),
(103, 'Michael Brown', 'michael.brown@email.com', '555-0103'),
(104, 'Emily Davis', 'emily.davis@email.com', '555-0104'),
(105, 'David Wilson', 'david.wilson@email.com', '555-0105');

-- ===================================================================
-- 3. SALES RELATION
-- ===================================================================
CREATE TABLE Sales (
    Sale_ID INT PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Book_ID INT NOT NULL,
    Date DATE NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID)
);

-- Insert tuples into Sales relation
INSERT INTO Sales (Sale_ID, Customer_ID, Book_ID, Date, Quantity) VALUES
(1001, 101, 1, '2026-05-10', 1),
(1002, 102, 3, '2026-05-12', 2),
(1003, 103, 2, '2026-05-15', 1),
(1004, 104, 5, '2026-05-18', 3),
(1005, 105, 4, '2026-05-20', 1),
(1006, 101, 3, '2026-05-22', 1),
(1007, 102, 1, '2026-05-24', 2);

-- ===================================================================
-- RELATIONAL SCHEMA SUMMARY
-- ===================================================================
-- 
-- BOOKS RELATION:
--   Attributes: Book_ID (Primary Key), Title, Author, Price
--   Tuples: 5 books in the database
--
-- CUSTOMERS RELATION:
--   Attributes: Customer_ID (Primary Key), Name, Email, Phone
--   Tuples: 5 customers in the database
--
-- SALES RELATION:
--   Attributes: Sale_ID (Primary Key), Customer_ID (Foreign Key), 
--               Book_ID (Foreign Key), Date, Quantity
--   Tuples: 7 sales transactions in the database
--   Relationships: Links Books and Customers through transactions
--
-- ===================================================================

-- ===================================================================
-- SAMPLE QUERIES TO VERIFY DATA
-- ===================================================================

-- View all books
-- SELECT * FROM Books;

-- View all customers
-- SELECT * FROM Customers;

-- View all sales
-- SELECT * FROM Sales;

-- View sales with book and customer details
-- SELECT 
--     s.Sale_ID,
--     c.Name AS Customer_Name,
--     b.Title AS Book_Title,
--     s.Date,
--     s.Quantity,
--     (s.Quantity * b.Price) AS Total_Amount
-- FROM Sales s
-- JOIN Customers c ON s.Customer_ID = c.Customer_ID
-- JOIN Books b ON s.Book_ID = b.Book_ID
-- ORDER BY s.Date DESC;
