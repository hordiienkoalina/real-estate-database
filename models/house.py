# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean
# Import the relationship function from the sqlalchemy.orm module
from sqlalchemy.orm import relationship
# Import the Base class from the models.base module
from models.base import Base

# Create a House class that inherits from the Base class
class House(Base):
    # Set the table name for this model in the database
    __tablename__ = "houses"

    # Define the columns for the houses table
    id = Column(Integer, primary_key=True)             # Primary key
    seller_name = Column(String, nullable=False)       # Seller name (non-nullable)
    bedrooms = Column(Integer, nullable=False)         # Number of bedrooms (non-nullable)
    bathrooms = Column(Integer, nullable=False)        # Number of bathrooms (non-nullable)
    listing_price = Column(Float, nullable=False)      # Listing price (non-nullable)
    zip_code = Column(String, nullable=False)          # Zip code (non-nullable)
    date_of_listing = Column(Date, nullable=False)     # Date of listing (non-nullable)
    sold = Column(Boolean, default=False)              # Sold status (default to False)

    # Foreign keys
    listing_agent_id = Column(Integer, ForeignKey("estate_agents.id"), nullable=False) # Listing agent ID (non-nullable)
    office_id = Column(Integer, ForeignKey("offices.id"), nullable=False)             # Office ID (non-nullable)

    # Relationships
    listing_agent = relationship("EstateAgent", back_populates="listings")  # One-to-many relationship with the EstateAgent model
    office = relationship("Office", back_populates="listings")              # One-to-many relationship with the Office model
    sale = relationship("Sale", back_populates="house", uselist=False)      # One-to-one relationship with the Sale model
