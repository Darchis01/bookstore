# Bookstore Database Design - Relations and Tuples

## Overview
This document defines the relational schema for a bookstore database system with three main relations: **Books**, **Customers**, and **Sales**.

---

## 1. BOOKS RELATION

### Relation Schema
```
Books (Book_ID, Title, Author, Price)
```

### Attributes:
- **Book_ID**: Unique identifier for each book (Primary Key, INT)
- **Title**: Name of the book (VARCHAR)
- **Author**: Name of the book's author (VARCHAR)
- **Price**: Cost of the book in dollars (DECIMAL)

### Tuples (Sample Data):

| Book_ID | Title | Author | Price |
|---------|-------|--------|-------|
| 1 | To Kill a Mockingbird | Harper Lee | $12.99 |
| 2 | 1984 | George Orwell | $13.99 |
| 3 | The Great Gatsby | F. Scott Fitzgerald | $11.99 |
| 4 | Pride and Prejudice | Jane Austen | $10.99 |
| 5 | The Catcher in the Rye | J.D. Salinger | $14.99 |

**Total Tuples: 5**

---

## 2. CUSTOMERS RELATION

### Relation Schema
```
Customers (Customer_ID, Name, Email, Phone)
```

### Attributes:
- **Customer_ID**: Unique identifier for each customer (Primary Key, INT)
- **Name**: Full name of the customer (VARCHAR)
- **Email**: Email address of the customer (VARCHAR)
- **Phone**: Contact phone number (VARCHAR)

### Tuples (Sample Data):

| Customer_ID | Name | Email | Phone |
|-------------|------|-------|-------|
| 101 | John Smith | john.smith@email.com | 555-0101 |
| 102 | Sarah Johnson | sarah.johnson@email.com | 555-0102 |
| 103 | Michael Brown | michael.brown@email.com | 555-0103 |
| 104 | Emily Davis | emily.davis@email.com | 555-0104 |
| 105 | David Wilson | david.wilson@email.com | 555-0105 |

**Total Tuples: 5**

---

## 3. SALES RELATION

### Relation Schema
```
Sales (Sale_ID, Customer_ID, Book_ID, Date, Quantity)
```

### Attributes:
- **Sale_ID**: Unique identifier for each transaction (Primary Key, INT)
- **Customer_ID**: Reference to the customer who made the purchase (Foreign Key, INT)
- **Book_ID**: Reference to the book being purchased (Foreign Key, INT)
- **Date**: Date of the transaction (DATE)
- **Quantity**: Number of copies purchased (INT)

### Tuples (Sample Data):

| Sale_ID | Customer_ID | Book_ID | Date | Quantity |
|---------|-------------|---------|------|----------|
| 1001 | 101 | 1 | 2026-05-10 | 1 |
| 1002 | 102 | 3 | 2026-05-12 | 2 |
| 1003 | 103 | 2 | 2026-05-15 | 1 |
| 1004 | 104 | 5 | 2026-05-18 | 3 |
| 1005 | 105 | 4 | 2026-05-20 | 1 |
| 1006 | 101 | 3 | 2026-05-22 | 1 |
| 1007 | 102 | 1 | 2026-05-24 | 2 |

**Total Tuples: 7**

---

## Key Relationships

### Referential Integrity:
- The **Sales** table maintains referential integrity with both **Books** and **Customers** tables
- Each sale transaction must reference a valid customer and a valid book
- This prevents orphaned records and maintains data consistency

### Database Constraints:
1. **Primary Keys**: Ensure uniqueness of records
   - Books: Book_ID
   - Customers: Customer_ID
   - Sales: Sale_ID

2. **Foreign Keys**: Maintain relationships
   - Sales.Customer_ID → Customers.Customer_ID
   - Sales.Book_ID → Books.Book_ID

3. **Not Null Constraints**: Ensure required data
   - All attributes in Books and Customers tables are NOT NULL
   - Key attributes in Sales table are NOT NULL

---

## Example Query Scenarios

### Scenario 1: Find all books purchased by a customer
```sql
SELECT b.Title, b.Author, b.Price, s.Quantity
FROM Sales s
JOIN Books b ON s.Book_ID = b.Book_ID
WHERE s.Customer_ID = 101;
```
**Result**: Books purchased by John Smith

### Scenario 2: Calculate total revenue per book
```sql
SELECT b.Title, SUM(s.Quantity * b.Price) AS Total_Revenue
FROM Sales s
JOIN Books b ON s.Book_ID = b.Book_ID
GROUP BY b.Book_ID, b.Title;
```

### Scenario 3: Get customer purchase history with details
```sql
SELECT 
    c.Name,
    b.Title,
    s.Date,
    s.Quantity,
    (s.Quantity * b.Price) AS Transaction_Total
FROM Sales s
JOIN Customers c ON s.Customer_ID = c.Customer_ID
JOIN Books b ON s.Book_ID = b.Book_ID
ORDER BY s.Date DESC;
```

---

## Summary Statistics

| Relation | Primary Key | Number of Tuples | Purpose |
|----------|------------|------------------|---------|
| Books | Book_ID | 5 | Maintain book inventory |
| Customers | Customer_ID | 5 | Store customer information |
| Sales | Sale_ID | 7 | Record purchase transactions |

---

## Database Design Principles Applied

1. **Normalization**: Each relation represents a single entity or relationship
2. **Primary Keys**: Unique identification for each record
3. **Foreign Keys**: Maintain referential integrity between relations
4. **Atomicity**: Each attribute contains atomic (indivisible) values
5. **Scalability**: Design can easily accommodate additional books, customers, or sales
