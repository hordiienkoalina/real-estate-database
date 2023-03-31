# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
# Import the relationship function from the sqlalchemy.orm module
from sqlalchemy.orm import relationship
# Import the Base class from the models.base module
from models.base import Base

# Create an Office class that inherits from the Base class
class Office(Base):
    # Set the table name for this model in the database
    __tablename__ = "offices"

    # Define the columns for the offices table
    id = Column(Integer, primary_key=True)           # Primary key
    name = Column(String, nullable=False)            # Office name (non-nullable)
    address = Column(String, nullable=False)         # Office address (non-nullable)

    # Relationships
    listings = relationship("House", back_populates="office") # One-to-many relationship with the House model