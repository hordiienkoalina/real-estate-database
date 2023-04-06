from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EstateAgent, House, Office, Sale, Commission
from queries.monthly_report import get_top_selling_agents, get_top_offices, get_monthly_sales_summary

DATABASE_URI = "sqlite:///real_estate.db"
engine = create_engine(DATABASE_URI)
session = Session(bind=engine)

month = 3
year = 2023

# Top selling agents
print(f"\nTop selling agents for {month}/{year}:")
top_selling_agents = get_top_selling_agents(session, month, year)
for idx, (agent, num_sales) in enumerate(top_selling_agents, start=1):
    print(f"{idx}. {agent.name} - {num_sales} sales")

# Top offices
print(f"\nTop offices for {month}/{year}:")
top_offices = get_top_offices(session, month, year)
for idx, (office, num_sales) in enumerate(top_offices, start=1):
    print(f"{idx}. {office.name} - {num_sales} sales")

# Monthly sales summary
print(f"\nMonthly sales summary for {month}/{year}:")
monthly_sales_summary = get_monthly_sales_summary(session, month, year)

print(f"Average number of days on the market per sold house: {monthly_sales_summary['avg_days_on_market']}")
print(f"Average selling price: ${monthly_sales_summary['avg_selling_price']:.2f}")