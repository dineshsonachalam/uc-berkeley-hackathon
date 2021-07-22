from sqlalchemy import create_engine, MetaData, Table, text, inspect
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

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

def get_male_count():
    try:
        table, session = get_sql_session()
        male_count = session.query(table).filter_by(sex='Male').count()
        return male_count
    except Exception as e:
        print("Exception: ", e)

def get_female_count():
    try:
        table, session = get_sql_session()
        female_count = session.query(table).filter_by(sex='Female').count()
        return female_count
    except Exception as e:
        print("Exception: ", e)

def get_relationship_stats():
    try:
        table, session = get_sql_session()
        wife_count = session.query(table).filter_by(relationship='Wife').count()
        own_child_count = session.query(table).filter_by(relationship='Own-child').count()
        husband_count = session.query(table).filter_by(relationship='Husband').count()
        not_in_family_count = session.query(table).filter_by(relationship='Not-in-family').count()
        other_relative_count = session.query(table).filter_by(relationship='Other-relative').count()
        unmarried_count = session.query(table).filter_by(relationship='Unmarried').count()
        return wife_count,own_child_count,husband_count,not_in_family_count,other_relative_count,unmarried_count
    except Exception as e:
        print("Exception: ", e)

def get_adult_data():
    try:
        table, session = get_sql_session()
        adults_info = session.query(table).with_entities(table.c.id, table.c.age, table.c.sex, table.c.salary, table.c.native_country,  table.c.education, table.c.marital_status).limit(100).all()
        data = []
        for id, age, sex, salary, native_country, education, marital_status in adults_info:
            data.append({
                "id": id,
                "age": age,
                "sex": sex,
                "salary": salary,
                "native_country": native_country,
                "education": education,
                "marital_status": marital_status
            })

        return data
    except Exception as e:
        print("Exception: ", e)