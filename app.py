from sqlalchemy import create_engine, MetaData, Table, func, text, inspect
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
import json

SQLALCHEMY_DATABASE_URL = "postgresql://dinesh:simple@postgres:5432/dinesh-micro-apps"

def get_sql_session():
    # Define the MySQL engine using MySQL Connector/Python
    db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
    metadata = MetaData()
    table = Table('adult', metadata, autoload=True, autoload_with=db)  
    session = sessionmaker(bind=db)
    session = session()
    return table, session

def check_if_table_exists():
    try:
        table = 'adult'
        db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
        return inspect(db).has_table(table)
    except Exception as e:
        print("Exception: ", e)

def check_if_table_is_empty():
    try:
        table, session = get_sql_session()
        table_count = session.query(table).count()
        if table_count>1:
            return False
        else:
            return True
    except Exception as e:
        print("Exception: ", e)

def execute_sql_file():
    if((check_if_table_exists() == False) or (check_if_table_is_empty() == True)):
        db = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=NullPool)
        file = open("./adult_dataset.sql")
        query = text(file.read())
        session = sessionmaker(bind=db)
        session = session()
        session.execute(query)

if __name__ == "__main__":
    try:
        execute_sql_file()
    except Exception as e:
        print("Exception: ", e)