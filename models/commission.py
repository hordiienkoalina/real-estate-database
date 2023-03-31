# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Float
# Import the Base class from the models.base module
from models.base import Base

# Create a Commission class that inherits from the Base class
class Commission(Base):
    # Set the table name for this model in the database
    __tablename__ = "commissions"

    # Define the columns for the commissions table
    id = Column(Integer, primary_key=True)       # Primary key
    amount = Column(Float, nullable=False)       # Commission amount (non-nullable)

    # Define the foreign key relationship between the commissions and sales tables
    sale_id = Column(Integer, ForeignKey("sales.id"), nullable=False)