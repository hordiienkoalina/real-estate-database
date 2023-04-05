from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import EstateAgent, Sale
from models import Office, House, Sale

def get_top_selling_agents(session, month, year, limit=5):
    selling_agents = (
        session.query(EstateAgent, func.count(Sale.id).label("num_sales"))
        .join(Sale, EstateAgent.id == Sale.selling_agent_id)
        .filter(func.extract("year", Sale.date_of_sale) == year)
        .filter(func.extract("month", Sale.date_of_sale) == month)
        .group_by(EstateAgent.id)
        .order_by(desc("num_sales"))
        .limit(limit)
        .all()
    )
    return selling_agents

def get_top_offices(session, month, year, limit=3):
    top_offices = (
        session.query(Office, func.count(Sale.id).label("num_sales"))
        .join(House, House.office_id == Office.id)
        .join(Sale, Sale.house_id == House.id)
        .filter(func.extract("year", Sale.date_of_sale) == year)
        .filter(func.extract("month", Sale.date_of_sale) == month)
        .group_by(Office.id)
        .order_by(desc("num_sales"))
        .limit(limit)
        .all()
    )
    return top_offices

def get_monthly_sales_summary(session: Session, month: str, year: str):
    monthly_sales = (
        session.query(func.count(Sale.id).label("num_sales"), func.sum(Sale.sale_price).label("total_sales"))
        .filter(func.extract("year", Sale.date_of_sale) == year)
        .filter(func.extract("month", Sale.date_of_sale) == month)
        .one()
    )

    return monthly_sales