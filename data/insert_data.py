from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from data.test_data_generator import generate_estate_agent_data, generate_house_data, generate_office_data, generate_sale_data, generate_commission_data
from models import EstateAgent, House, Office, Sale, Commission

DATABASE_URI = "sqlite:///real_estate.db"

engine = create_engine(DATABASE_URI)
session = Session(bind=engine)

# Insert EstateAgents
for _ in range(5):
    agent_data = generate_estate_agent_data()
    agent = EstateAgent(**agent_data)
    session.add(agent)

session.commit()

# Insert Offices
for _ in range(3):
    office_data = generate_office_data()
    office = Office(**office_data)
    session.add(office)

session.commit()

# Insert Houses
estate_agents = session.query(EstateAgent).all()
offices = session.query(Office).all()

for agent in estate_agents:
    for office in offices:
        house_data = generate_house_data(agent.id, office.id)
        house = House(**house_data)
        session.add(house)

session.commit()

# Insert Sales and Commissions
houses = session.query(House).all()
selling_agents = estate_agents

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