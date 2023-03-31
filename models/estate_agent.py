# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
# Import the relationship function from the sqlalchemy.orm module
from sqlalchemy.orm import relationship
# Import the Base class from the models.base module
from models.base import Base

# Create an EstateAgent class that inherits from the Base class
class EstateAgent(Base):
    # Set the table name for this model in the database
    __tablename__ = "estate_agents"

    # Define the columns for the estate_agents table
    id = Column(Integer, primary_key=True)      # Primary key
    name = Column(String, nullable=False)       # Agent name (non-nullable)
    email = Column(String, nullable=False)      # Agent email (non-nullable)
    phone = Column(String, nullable=False)      # Agent phone (non-nullable)

    # Define the relationships between the EstateAgent model and other models
    listings = relationship("House", back_populates="listing_agent")  # One-to-many relationship with the House model
    sales = relationship("Sale", back_populates="selling_agent")      # One-to-many relationship with the Sale model