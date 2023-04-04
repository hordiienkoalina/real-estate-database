from faker import Faker

fake = Faker()

# Generates fake data for an estate agent and returns a dictionary with the required fields.
def generate_estate_agent_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }

# Generates fake data for an office and returns a dictionary with the required fields.
def generate_office_data():
    return {
        "name": fake.company(),
        "address": fake.address()
    }

# Generates fake data for a house and returns a dictionary with the required fields.
# estate_agent_id: ID of the estate agent who lists the house
# office_id: ID of the office that lists the house
def generate_house_data(estate_agent_id, office_id):
    return {
        "seller_name": fake.name(),
        "bedrooms": fake.random_int(min=1, max=5),
        "bathrooms": fake.random_int(min=1, max=3),
        "listing_price": fake.random_int(min=50000, max=500000),
        "zip_code": fake.zipcode(),
        "date_of_listing": fake.date_between(start_date='-1y', end_date='today'),
        "listing_agent_id": estate_agent_id,
        "office_id": office_id
    }

# Generates fake data for a sale and returns a dictionary with the required fields.
# house_id: ID of the house being sold
# selling_agent_id: ID of the agent who sells the house
def generate_sale_data(house_id, selling_agent_id):
    return {
        "buyer_name": fake.name(),
        "sale_price": fake.random_int(min=50000, max=500000),
        "date_of_sale": fake.date_between(start_date='-1y', end_date='today'),
        "house_id": house_id,
        "selling_agent_id": selling_agent_id
    }

# Generates fake data for a commission and returns a dictionary with the required fields.
# sale_id: ID of the sale associated with the commission
def generate_commission_data(sale_id):
    return {
        "amount": fake.random_int(min=1000, max=10000),
        "sale_id": sale_id
    }