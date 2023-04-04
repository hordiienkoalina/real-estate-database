from faker import Faker

fake = Faker()

def generate_estate_agent_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
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
        "office_id": office_id
    }

def generate_sale_data(house_id, selling_agent_id):
    return {
        "buyer_name": fake.name(),
        "sale_price": fake.random_int(min=50000, max=500000),
        "date_of_sale": fake.date_between(start_date='-1y', end_date='today'),
        "house_id": house_id,
        "selling_agent_id": selling_agent_id
    }

def generate_commission_data(sale_id):
    return {
        "amount": fake.random_int(min=1000, max=10000),
        "sale_id": sale_id
    }