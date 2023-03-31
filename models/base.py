# Import the declarative_base function from the SQLAlchemy library
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for all the ORM models to inherit from
Base = declarative_base()