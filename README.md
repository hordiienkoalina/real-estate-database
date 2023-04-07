# Real Estate Database
GitHub Link: https://github.com/hordiienkoalina/real-estate-database

## Description

This Real Estate Database System is a comprehensive solution to manage property listings, sales, and commissions for a large franchised real estate company with multiple offices across the country. It is built using Python, SQLAlchemy, and SQLite, providing a lightweight and efficient tool to handle complex data relationships and generate insightful reports.

### Features

1. **Property Listings**: Captures and stores relevant details of each listed property, including seller details, number of bedrooms and bathrooms, listing price, zip code, date of listing, the listing estate agent, and the appropriate office.
2. **Property Sales**: Records sales information such as buyer details, sale price, date of sale, and the selling estate agent. It also marks the original listing as sold and calculates the estate agent's commission based on a sliding scale.
3. **Reporting**: Generates monthly reports, including the top 5 offices and estate agents based on sales, the commission for each estate agent, the average number of days on the market for sold properties, and the average selling price for the month.
4. **Testing**: Uses Python's unittest module to test the accuracy of its data manipulation and calculations by working with generated fictitious data.

### Tech Stack

- **Backend**: Python 3, SQLAlchemy.
- **Database**: SQLite.
- **Testing**: Python's unittest module.
- **Data Generation**: Faker library.

## Install

macOS:
```
python3 -m venv test-venv
source test-venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 -m data.insert_data
python3 -m queries.run_queries
```

Windows:
```
python3 -m venv test-venv
test-venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 create.py
python3 -m data.insert_data
python3 -m queries.run_queries
```

## Read DB

```
sqlite3 real_estate.db
.tables
SELECT * FROM <table_name>;
.quit
```
Alternatively, you may use the SQLite Viewer extension in Visual Studio Code.

## Test

The following scripts for the accuracy of the commission calculations and the correctness of data retrieval by specified month.

```
python3 -m unittest tests/test_commission.py
python3 -m unittest tests/test_test_month.py
```

##  ✨ Technicalities ✨

### Data Normalisation
1. The database schema follows the principles of normalization. For example, the estate agent, office, house, and sale information is separated into respective tables; primary keys identify their unique records and foreign keys establish relationships between tables.
2. The use of separate tables for storing commission information ensures that commission calculations are not duplicated and are easy to maintain. 

### Indices
Indices have been added to the foreign keys to optimize search queries and improve the performance of join operations between tables. For instance, indices on the ```office_id``` and ```listing_agent_id``` in the House table, and on the ```selling_agent_id``` and ```house_id``` in the Sale table, help speed up the retrieval of related data.

### Transactions
In ```insert_data.py```, transactions are used to ensure that all data insertions are atomic, consistent, isolated, and durable (ACID). For example, after inserting sales data into the Sale table, a commit operation is performed before inserting the related commission data into the Commission table. This ensures that the insertion of sales and commission data occurs as a single, indivisible operation, maintaining data integrity.

## Limitations
Apart from all the impressive and useful features this tool offers, it has one drawback: the month of interest is hardcoded into run_queries.py. A more user-friendly approach would be to request the month of interest from the user through the Terminal, rather than having it hardcoded.

## Policy for the use of AI tools at MU as of 3/17/2023
In this assignment, I used ChatGPT in the debugging process for such tasks as decoding lengthy error messages, and generally interpreting error messages and their potential causes. I also used it to help generate descriptions, such as expanding on my code comments in some files, and stringing my ```README.md``` draft bullet points to create a cohesive narrative.