# Bookstore Database - Entity-Relationship Diagram & Data Flow

## ER Diagram (Text Representation)

```
┌─────────────────────────────────────────────────────────────────┐
│                         BOOKSTORE DATABASE                       │
└─────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────┐
                    │      BOOKS           │
                    ├──────────────────────┤
                    │ PK: Book_ID (INT)    │
                    │ - Title (VARCHAR)    │
                    │ - Author (VARCHAR)   │
                    │ - Price (DECIMAL)    │
                    └──────────┬───────────┘
                               │
                               │ (1:M)
                               │ Book_ID
                               │
                    ┌──────────▼────────────┐
                    │       SALES           │
                    ├──────────────────────┤
                    │ PK: Sale_ID (INT)    │
                    │ FK: Customer_ID (INT)│◄─────────┐
                    │ FK: Book_ID (INT)    │          │
                    │ - Date (DATE)        │          │ (1:M)
                    │ - Quantity (INT)     │          │ Customer_ID
                    └──────────┬───────────┘          │
                               │                       │
                               │ (M:1)                 │
                               │ Customer_ID           │
                               │                       │
                    ┌──────────▼────────────────────┐
                    │     CUSTOMERS                │
                    ├──────────────────────────────┤
                    │ PK: Customer_ID (INT)        │
                    │ - Name (VARCHAR)             │
                    │ - Email (VARCHAR)            │
                    │ - Phone (VARCHAR)            │
                    └──────────────────────────────┘

Legend:
  PK = Primary Key
  FK = Foreign Key
  1:M = One-to-Many Relationship
  M:1 = Many-to-One Relationship
```

---

## Relationship Descriptions

### 1. Books → Sales (1:M)
**One Book → Many Sales**
- One book can be sold multiple times
- Example: Book 1 ("To Kill a Mockingbird") appears in Sales records 1001, 1006

### 2. Customers → Sales (1:M)
**One Customer → Many Sales**
- One customer can purchase multiple times
- Example: Customer 101 (John Smith) appears in Sales records 1001, 1006

### 3. Sales Table (Junction Table)
- Connects Books and Customers
- Represents the M:M (Many-to-Many) relationship between them
- Each sale record captures: WHO bought WHAT and WHEN

---

## Data Flow Diagram

```
                        ┌─────────────────┐
                        │   BOOKSTORE     │
                        └────────┬────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼
        ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
        │   BOOKS      │  │  CUSTOMERS  │  │    SALES     │
        ├──────────────┤  ├─────────────┤  ├──────────────┤
        │ Book_ID (PK) │  │Customer_ID  │  │ Sale_ID (PK) │
        │ Title        │  │ (PK)        │  │Customer_ID   │
        │ Author       │  │ Name        │  │(FK→Customers)│
        │ Price        │  │ Email       │  │Book_ID       │
        │              │  │ Phone       │  │(FK→Books)    │
        │              │  │             │  │ Date         │
        │              │  │             │  │ Quantity     │
        └──────────────┘  └─────────────┘  └──────────────┘
              ▲                  ▲                │
              │                  │                │
              │ Input: New Books │ Input:        │
              │ Inventory        │ New Customers │
              │ Catalog Items    │ Registration  │
              │                  │                │
              │                  └────────────────┘
              │                    Output: 
              │                    Transaction Records
              └────────────────────────────────────────
                   Output: 
                   Sales Reports & Analytics
```

---

## Transaction Example

### Scenario: Customer 102 (Sarah Johnson) purchases 2 copies of Book 3 (The Great Gatsby)

**Step 1**: Check BOOKS table for Book_ID = 3
```
Book_ID: 3
Title: The Great Gatsby
Author: F. Scott Fitzgerald
Price: $11.99
```

**Step 2**: Check CUSTOMERS table for Customer_ID = 102
```
Customer_ID: 102
Name: Sarah Johnson
Email: sarah.johnson@email.com
Phone: 555-0102
```

**Step 3**: Create new SALES tuple (Sale_ID = 1002)
```
Sale_ID: 1002
Customer_ID: 102 (FK to Customers)
Book_ID: 3 (FK to Books)
Date: 2026-05-12
Quantity: 2
```

**Step 4**: Calculate transaction details
```
Unit Price: $11.99
Quantity: 2
Transaction Total: 2 × $11.99 = $23.98
```

---

## Cardinality Relationships

### Books to Sales
- **1:M** (One-to-Many)
- One book record can have multiple sales records
- Constraint: Each sale must reference exactly one book

### Customers to Sales  
- **1:M** (One-to-Many)
- One customer record can have multiple sales records
- Constraint: Each sale must reference exactly one customer

### Books to Customers (through Sales)
- **M:M** (Many-to-Many)
- One book can be purchased by many customers
- One customer can purchase many books
- The SALES table acts as a junction table

---

## Integrity Constraints

### Domain Constraints
- Book_ID, Customer_ID, Sale_ID: Must be positive integers
- Price, Quantity: Must be positive numbers
- Date: Must be in valid date format

### Key Constraints
- Book_ID must be unique in BOOKS table
- Customer_ID must be unique in CUSTOMERS table
- Sale_ID must be unique in SALES table

### Referential Integrity Constraints
- Sales.Customer_ID must exist in Customers.Customer_ID
- Sales.Book_ID must exist in Books.Book_ID
- Deleting a customer or book should be restricted if related sales exist

### Entity Integrity Constraints
- All primary keys must have values (NOT NULL)
- No duplicate primary keys allowed

---

## Query Examples with Data Flow

### Query 1: Show what John Smith bought
```
Input: Customer_ID = 101 (John Smith)
Process: 
  1. Find all Sales records where Customer_ID = 101
  2. For each sale, retrieve Book details using Book_ID
Output: 
  - Sale 1001: To Kill a Mockingbird (1 copy) on 2026-05-10
  - Sale 1006: The Great Gatsby (1 copy) on 2026-05-22
```

### Query 2: Show which customers bought "1984"
```
Input: Title = "1984"
Process:
  1. Find Book_ID for "1984" (Book_ID = 2)
  2. Find all Sales records where Book_ID = 2
  3. For each sale, retrieve Customer details
Output:
  - Sale 1003: Michael Brown purchased 1 copy on 2026-05-15
```

### Query 3: Calculate monthly sales revenue
```
Input: Date range (all May 2026 sales)
Process:
  1. Sum (Quantity × Price) for all sales in month
  2. Group by date or book
Output:
  - Total Revenue: Sum of all transactions
  - Per-Book Revenue: Revenue breakdown by title
  - Per-Customer Revenue: Revenue breakdown by customer
```
