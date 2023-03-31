# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
# Import the Base class and the models
from models import Base, EstateAgent, House, Office, Sale, Commission

# Define the database URI for SQLite
DATABASE_URI = "sqlite:///real_estate.db"

# Define the main function
def main():
    # Create the engine using the database URI
    engine = create_engine(DATABASE_URI)
    # Create all the tables based on the models using the engine
    Base.metadata.create_all(engine)
    # Print a success message
    print("Database tables created successfully.")

# If this script is run as the main module, execute the main function
if __name__ == "__main__":
    main()