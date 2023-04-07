# Import neccessary modules
import unittest
from models.commission import Commission
from data.test_data_generator import generate_commission_data
from queries.utils import calculate_commission
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base

# Define the test database URL
TEST_DATABASE_URL = "sqlite:///test_database.db"

class TestCommissionCalculation(unittest.TestCase):

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

    def test_calculate_commission(self):
        test_cases = [
            (95000, 0.10),
            (150000, 0.075),
            (350000, 0.06),
            (800000, 0.05),
            (1500000, 0.04),
        ]

        # Test commission calculation for each test case
        for sale_price, expected_rate in test_cases:
            with self.subTest(sale_price=sale_price, expected_rate=expected_rate):
                expected_commission = sale_price * expected_rate
                calculated_commission = calculate_commission(sale_price)
                self.assertEqual(calculated_commission, expected_commission)

    def test_generate_commission_data(self):
        sale_id = 1
        sale_price = 250000
        expected_commission = calculate_commission(sale_price)

        # Test commission data generation
        commission_data = generate_commission_data(sale_id, sale_price)
        self.assertEqual(commission_data["amount"], expected_commission)
        self.assertEqual(commission_data["sale_id"], sale_id)

    def test_insert_commission(self):
        # Add a test sale and commission to the database
        sale_id = 1
        sale_price = 250000
        commission_data = generate_commission_data(sale_id, sale_price)
        commission = Commission(**commission_data)

        # Insert the commission to the database
        self.session.add(commission)
        self.session.commit()

        # Retrieve the commission from the database and assert the amount and sale_id
        inserted_commission = self.session.query(Commission).filter(Commission.sale_id == sale_id).one()
        self.assertEqual(inserted_commission.amount, commission_data["amount"])
        self.assertEqual(inserted_commission.sale_id, commission_data["sale_id"])

if __name__ == "__main__":
    unittest.main()