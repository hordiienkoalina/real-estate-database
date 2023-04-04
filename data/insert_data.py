from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from data.test_data_generator import generate_estate_agent_data, generate_house_data, generate_office_data, generate_sale_data, generate_commission_data
from models import EstateAgent, House, Office, Sale, Commission

DATABASE_URI = "sqlite:///real_estate.db"

engine = create_engine(DATABASE_URI)
session = Session(bind=engine)

# Insert EstateAgents
# Generate and insert 5 fake estate agents into the database
for _ in range(5):
    agent_data = generate_estate_agent_data()
    agent = EstateAgent(**agent_data)
    session.add(agent)

session.commit()

# Insert Offices
# Generate and insert 3 fake offices into the database
for _ in range(3):
    office_data = generate_office_data()
    office = Office(**office_data)
    session.add(office)

session.commit()

# Insert Houses
# Query all estate agents and offices from the database
estate_agents = session.query(EstateAgent).all()
offices = session.query(Office).all()

# Generate and insert fake houses for each combination of estate agent and office
for agent in estate_agents:
    for office in offices:
        house_data = generate_house_data(agent.id, office.id)
        house = House(**house_data)
        session.add(house)

session.commit()

# Insert Sales and Commissions
# Query all houses from the database
houses = session.query(House).all()
selling_agents = estate_agents

# Generate and insert fake sales and commissions for each combination of house and selling agent
for house in houses:
    for agent in selling_agents:
        sale_data = generate_sale_data(house.id, agent.id)
        sale = Sale(**sale_data)
        session.add(sale)
        session.commit()  # Commit the Sale object to the session

        commission_data = generate_commission_data(sale.id)
        commission = Commission(**commission_data)
        session.add(commission)

session.commit()

print("Test data has been inserted successfully.")