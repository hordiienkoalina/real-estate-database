import unittest
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base
from models import House, Sale
from queries.monthly_report import get_monthly_sales_summary

TEST_DATABASE_URL = "sqlite:///test_database.db"

class TestMonthlyReport(unittest.TestCase):

    def setUp(self):
        # Set up the test database and session
        self.engine = create_engine(TEST_DATABASE_URL)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        # Close the session and drop the test database
        self.session.close()
        Base.metadata.drop_all(self.engine)

def test_get_monthly_sales_summary(self):
    # Create test data
    house = House(id=1, seller_name="John Doe", bedrooms=3, bathrooms=2, listing_price=320000, zip_code="12345", date_of_listing=datetime(2023, 2, 1), sold=False, listing_agent_id=1, office_id=1)
    sale = Sale(id=1, house_id=1, date_of_sale=datetime(2023, 3, 1), sale_price=300000)

    self.session.add(house)
    self.session.add(sale)
    self.session.commit()

    # Query the test data using get_monthly_sales_summary
    summary = get_monthly_sales_summary(self.session, 3, 2023)

    # Assert that the returned summary matches the expected values
    self.assertEqual(summary["avg_days_on_market"], 28)
    self.assertEqual(summary["avg_selling_price"], 300000)
        
if __name__ == "__main__":
    unittest.main()
