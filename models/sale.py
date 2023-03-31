# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
# Import the relationship function from the sqlalchemy.orm module
from sqlalchemy.orm import relationship
# Import the Base class from the models.base module
from models.base import Base

# Create a Sale class that inherits from the Base class
class Sale(Base):
    # Set the table name for this model in the database
    __tablename__ = "sales"

    # Define the columns for the sales table
    id = Column(Integer, primary_key=True)                       # Primary key
    buyer_name = Column(String, nullable=False)                  # Buyer's name (non-nullable)
    sale_price = Column(Float, nullable=False)                   # Sale price (non-nullable)
    date_of_sale = Column(Date, nullable=False)                  # Date of sale (non-nullable)

    # Foreign keys
    house_id = Column(Integer, ForeignKey("houses.id"), nullable=False)         # Foreign key referencing the House model
    selling_agent_id = Column(Integer, ForeignKey("estate_agents.id"), nullable=False) # Foreign key referencing the EstateAgent model

    # Relationships
    house = relationship("House", back_populates="sale")         # One-to-one relationship with the House model
    selling_agent = relationship("EstateAgent", back_populates="sales") # One-to-many relationship with the EstateAgent model