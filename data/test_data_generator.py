# Import neccessary modules
from faker import Faker
from queries.utils import calculate_commission
from models import House

fake = Faker()

def generate_estate_agent_data(office_id):
    # Generate random estate agent data including name, email, phone number, and office_id
    return {
        "name": f"{fake.first_name()} {fake.last_name()}",
        "email": fake.email(),
        "phone": fake.phone_number(),
        "office_id": office_id
    }

def generate_office_data():
    # Generate random office data including name and address
    return {
        "name": fake.company(),
        "address": fake.address()
    }

def generate_house_data(selling_agent_id, office_id):
    # Generate random house data with various attributes
    return {
        "seller_name": fake.name(),
        "bedrooms": fake.random_int(min=1, max=5),
        "bathrooms": fake.random_int(min=1, max=3),
        "listing_price": fake.random_int(min=50000, max=500000),
        "zip_code": fake.zipcode(),
        "date_of_listing": fake.date_between(start_date='-1y', end_date='today'),
        "listing_agent_id": selling_agent_id,
        "office_id": office_id,
        "sold": fake.boolean(chance_of_getting_true=50)
    }

def generate_sale_data(house_id, selling_agent_id, session):
    # Fetch the date_of_listing for the given house_id
    date_of_listing = session.query(House.date_of_listing).filter(House.id == house_id).scalar()
    # Generate a random date_of_sale after the date_of_listing
    date_of_sale = fake.date_between(start_date=date_of_listing, end_date='today')
    sale_price = fake.random_int(min=50000, max=500000)
    
    # Generate random sale data with various attributes
    return {
        "buyer_name": fake.name(),
        "sale_price": sale_price,
        "date_of_sale": date_of_sale,
        "house_id": house_id,
        "selling_agent_id": selling_agent_id
    }

def generate_commission_data(sale_id, sale_price):
    # Calculate commission amount based on sale price
    amount = calculate_commission(sale_price)
    # Generate commission data with amount and sale_id
    return {
        "amount": amount,
        "sale_id": sale_id
    }