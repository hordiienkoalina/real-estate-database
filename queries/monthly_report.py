# Import necessary modules
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import EstateAgent, Sale
from models import Office, House, Sale

# Function to get the top selling agents for a given month and year
def get_top_selling_agents(session, month, year, limit=5):
    selling_agents = (
        # Query the EstateAgent model and count the number of sales per agent
        session.query(EstateAgent, func.count(Sale.id).label("num_sales"))
        # Join the Sale model on the selling agent's ID
        .join(Sale, EstateAgent.id == Sale.selling_agent_id)
        # Filter the sales based on the given year
        .filter(func.extract("year", Sale.date_of_sale) == year)
        # Filter the sales based on the given month
        .filter(func.extract("month", Sale.date_of_sale) == month)
        # Group the results by the estate agent's ID
        .group_by(EstateAgent.id)
        # Order the results by the number of sales in descending order
        .order_by(desc("num_sales"))
        # Limit the number of results
        .limit(limit)
        # Fetch all the results
        .all()
    )
    return selling_agents

# Function to get the top offices for a given month and year
def get_top_offices(session, month, year, limit=3):
    top_offices = (
        # Query the Office model and count the number of sales per office
        session.query(Office, func.count(Sale.id).label("num_sales"))
        # Join the House model on the office's ID
        .join(House, House.office_id == Office.id)
        # Join the Sale model on the house's ID
        .join(Sale, Sale.house_id == House.id)
        # Filter the sales based on the given year
        .filter(func.extract("year", Sale.date_of_sale) == year)
        # Filter the sales based on the given month
        .filter(func.extract("month", Sale.date_of_sale) == month)
        # Group the results by the office's ID
        .group_by(Office.id)
        # Order the results by the number of sales in descending order
        .order_by(desc("num_sales"))
        # Limit the number of results
        .limit(limit)
        # Fetch all the results
        .all()
    )
    return top_offices

# Function to get the monthly sales summary for a given month and year
def get_monthly_sales_summary(session: Session, month: str, year: str):
    result = (
        # Query to calculate the average number of days on the market and the average selling price
        session.query(
            func.avg(Sale.date_of_sale - House.date_of_listing).label("avg_days_on_market"),
            func.avg(Sale.sale_price).label("avg_selling_price"),
        )
        # Select from the Sale model
        .select_from(Sale)
        # Join the House model on the house's ID
        .join(House, House.id == Sale.house_id)
        # Filter the sales based on the given year
        .filter(func.extract("year", Sale.date_of_sale) == year)
        # Filter the sales based on the given month
        .filter(func.extract("month", Sale.date_of_sale) == month)
        # Fetch the result
        .one()
    )

    return {
        "avg_days_on_market": result.avg_days_on_market,
        "avg_selling_price": float(result.avg_selling_price),
    }