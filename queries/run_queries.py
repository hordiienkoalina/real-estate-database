# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from queries.monthly_report import get_top_selling_agents, get_top_offices, get_monthly_sales_summary

# Define the database connection string
DATABASE_URI = "sqlite:///real_estate.db"
# Create a connection to the database
engine = create_engine(DATABASE_URI)
# Create a session to interact with the database
session = Session(bind=engine)

# Define the month and year for the monthly report
month = 3
year = 2023

# Top selling agents
# Print a header for the top selling agents section
print(f"\nTop selling agents for {month}/{year}:")
# Query the database to get the top selling agents
top_selling_agents = get_top_selling_agents(session, month, year)
# Iterate over the top selling agents and print their name and number of sales
for idx, (agent, num_sales) in enumerate(top_selling_agents, start=1):
    print(f"{idx}. {agent.name} - {num_sales} sales")

# Top offices
# Print a header for the top offices section
print(f"\nTop offices for {month}/{year}:")
# Query the database to get the top offices
top_offices = get_top_offices(session, month, year)
# Iterate over the top offices and print their name and number of sales
for idx, (office, num_sales) in enumerate(top_offices, start=1):
    print(f"{idx}. {office.name} - {num_sales} sales")

# Monthly sales summary
# Print a header for the monthly sales summary section
print(f"\nMonthly sales summary for {month}/{year}:")
# Query the database to get the monthly sales summary
monthly_sales_summary = get_monthly_sales_summary(session, month, year)

# Print the average number of days on the market for sold houses
print(f"Average number of days on the market per sold house: {monthly_sales_summary['avg_days_on_market']}")
# Print the average selling price for sold houses
print(f"Average selling price: ${monthly_sales_summary['avg_selling_price']:.2f}")