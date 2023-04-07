from faker import Faker
from queries.utils import calculate_commission

fake = Faker()

def generate_estate_agent_data(office_id):
    return {
        "name": f"{fake.first_name()} {fake.last_name()}",
        "email": fake.email(),
        "phone": fake.phone_number(),
        "office_id": office_id
    }

def generate_office_data():
    return {
        "name": fake.company(),
        "address": fake.address()
    }

def generate_house_data(estate_agent_id, office_id):
    return {
        "seller_name": fake.name(),
        "bedrooms": fake.random_int(min=1, max=5),
        "bathrooms": fake.random_int(min=1, max=3),
        "listing_price": fake.random_int(min=50000, max=500000),
        "zip_code": fake.zipcode(),
        "date_of_listing": fake.date_between(start_date='-1y', end_date='today'),
        "listing_agent_id": estate_agent_id,
        "office_id": office_id,
        "sold": fake.boolean(chance_of_getting_true=50)
    }

def generate_sale_data(house_id, selling_agent_id):
    sale_price = fake.random_int(min=50000, max=500000)
    return {
        "buyer_name": fake.name(),
        "sale_price": sale_price,
        "date_of_sale": fake.date_between(start_date='-1y', end_date='today'),
        "house_id": house_id,
        "selling_agent_id": selling_agent_id
    }

def generate_commission_data(sale_id, sale_price):
    amount = calculate_commission(sale_price)
    return {
        "amount": amount,
        "sale_id": sale_id
    }