from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EstateAgent, House, Office, Sale, Commission
from queries.monthly_report import get_top_selling_agents, get_top_offices, get_monthly_sales_summary

DATABASE_URI = "sqlite:///real_estate.db"

engine = create_engine(DATABASE_URI)
session = Session(bind=engine)

month = "03"
year = "2023"

print(f"Top selling agents for {month}/{year}:")
top_selling_agents = get_top_selling_agents(session, month, year)
for idx, (agent, num_sales) in enumerate(top_selling_agents, start=1):
    print(f"{idx}. {agent.name} ({agent.email}) - {num_sales} sales")

print(f"\nTop offices for {month}/{year}:")
top_offices = get_top_offices(session, month, year)
for idx, (office, num_sales) in enumerate(top_offices, start=1):
    print(f"{idx}. {office.name} - {office.address} - {num_sales} sales")

print(f"\nMonthly sales summary for {month}/{year}:")
monthly_sales_summary = get_monthly_sales_summary(session, month, year)
print(monthly_sales_summary)