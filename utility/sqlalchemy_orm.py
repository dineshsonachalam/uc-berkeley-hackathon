from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime
from sqlalchemy.orm import sessionmaker
# Use already created database
engine = create_engine('sqlite:///adult_dataset.db', echo=False)
Base = declarative_base()

class Adult(Base):
    """"""
    __tablename__ = "adult" # Tablename

    # Initializing the columns for the table
    id = Column(Integer, primary_key=True)
    age = Column(String)
    workclass = Column(String)
    fnlwgt = Column(String)
    education = Column(String)
    education_num = Column(String)
    marital_status = Column(String)
    occupation = Column(String)
    relationship = Column(String)
    race = Column(String)
    sex = Column(String)
    capital_gain = Column(String)
    capital_loss = Column(String)
    hours_per_week = Column(String)
    native_country = Column(String)
    salary = Column(String)

    # Setting Default constructor __init__ that is called when an object is being created.
    def __init__(self, age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,
                 capital_loss,hours_per_week,native_country,salary):
        self.age = age
        self.workclass = workclass
        self.fnlwgt = fnlwgt
        self.education = education
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country
        self.salary = salary
    # create tables
    Base.metadata.create_all(engine)

    # Function to calculate total number of males and females
    def total_males_females(self):
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Initializing the male count and female count has 0
        male_count = 0
        female_count = 0
        # Select objects
        for adult in session.query(Adult):
            if(adult.sex == "Male"):
                male_count = male_count + 1
            else:
                female_count = female_count + 1
        # print("Male Count:",male_count)
        # print("Female Count:",female_count)
        total_count = [male_count,female_count]
        session.close()
        return total_count

    # Function to calculate total number of people in each relationship
    def total_people_in_relationship(self):

        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Select objects
        Wife_count = 0
        Own_child_count = 0
        Husband_count = 0
        Not_in_family_count = 0
        Other_relative_count = 0
        Unmarried_count = 0

        for adult in session.query(Adult):
            if(adult.relationship == "Wife"):
                Wife_count = Wife_count + 1
            elif(adult.relationship == "Own-child"):
                Own_child_count = Own_child_count + 1
            elif(adult.relationship == "Husband"):
                Husband_count = Husband_count + 1
            elif(adult.relationship == "Not-in-family"):
                Not_in_family_count = Not_in_family_count +1
            elif(adult.relationship == "Other-relative"):
                Other_relative_count = Other_relative_count + 1
            elif(adult.relationship == "Unmarried"):
                Unmarried_count = Unmarried_count + 1

        # print("Wife Count:",Wife_count)
        # print("Own_child_count",Own_child_count)
        # print("Husband_count",Husband_count)
        # print("Not_in_family_count",Not_in_family_count)
        # print("Other_relative_count",Other_relative_count)
        # print("Unmarried_count",Unmarried_count)
        total_people_count = [Wife_count,Own_child_count,Husband_count,Not_in_family_count,Other_relative_count,Unmarried_count]
        session.close()
        return total_people_count

    # Query all data from the database
    def query_all(self):
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        sql_query = """ select * from adult """
        print(sql_query)

        results = engine.execute(sql_query)
        query_result = []
        count = 1
        for result in results:
            if(count==30):
                break
            #print("Count:",count)
            age = result[1]
            workclass = result[2]
            fnlwgt = result[3]
            education = result[4]
            education_num= result[5]
            marital_status= result[6]
            occupation= result[7]
            relationship = result[8]
            race = result[9]
            sex = result[10] #
            capital_gain = result[11]
            capital_loss = result[12]
            hours_per_week= result[13]
            native_country = result[14]
            salary = result[15]

            # print("Age:", age)
            # print("Relationship:", relationship)
            # print("Race:", race)
            # print("Sex:", sex)
            # print("Native Country:", native_country)
            # print()
            query_result.append([age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,
                 capital_loss,hours_per_week,native_country,salary])
            count = count + 1
        session.close()
        return query_result

    # Query filter function when user chooses a filter in dropdown
    def query_filter(self,sex='',race='',relationship=''):
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        sql_query = """ select * from adult """
        if (len(sex) > 0 or len(race) > 0 or len(relationship) > 0):
            Flag = False
            sql_query = sql_query + """ where """
            # 1

            if (len(sex) > 0):
                sql_query = sql_query + """ ( """
                for i in range(0, len(sex)):
                    if (i == (len(sex) - 1)):
                        sql_query = sql_query + """ sex =""" + """ " """.strip() + str(sex[i]) + """ " """.strip()
                    else:
                        sql_query = sql_query + """ sex =""" + """ " """.strip() + str(
                            sex[i]) + """ " """.strip() + " OR"
                Flag = True
                sql_query = sql_query + """ ) """

                # 2

            if (len(race) > 0):
                if (Flag == True):
                    sql_query = sql_query + """ AND """
                sql_query = sql_query + """ ( """
                for i in range(0, len(race)):
                    if (i == (len(race) - 1)):
                        sql_query = sql_query + """ race =  """ + """ " """.strip() + str(race[i]) + """ " """.strip()
                    else:
                        sql_query = sql_query + """ race =  """ + """ " """.strip() + str(
                            race[i]) + """ " """.strip() + " OR"
                Flag = True
                sql_query = sql_query + """ ) """

                # 3
            if (len(relationship) > 0):
                if (Flag == True):
                    sql_query = sql_query + """ AND """
                sql_query = sql_query + """ ( """
                for i in range(0, len(relationship)):
                    if (i == (len(relationship) - 1)):
                        sql_query = sql_query + """ relationship =  """ + """ " """.strip() + str(
                            relationship[i]) + """ " """.strip()
                    else:
                        sql_query = sql_query + """ relationship =  """ + """ " """.strip() + str(
                            relationship[i]) + """ " """.strip() + " OR"
                Flag = True
                sql_query = sql_query + """ ) """

        print(sql_query)
        results = engine.execute(sql_query)
        query_result = []
        count = 1
        for result in results:
            if (count == 30):
                break
            count = count + 1
            age = result[1]
            workclass = result[2]
            fnlwgt = result[3]
            education = result[4]
            education_num = result[5]
            marital_status = result[6]
            occupation = result[7]
            relationship = result[8]
            race = result[9]
            sex = result[10]  #
            capital_gain = result[11]
            capital_loss = result[12]
            hours_per_week = result[13]
            native_country = result[14]
            salary = result[15]

            # print("Age:", age)
            # print("Relationship:", relationship)
            # print("Race:", race)
            # print("Sex:", sex)
            # print("Native Country:", native_country)
            # print()
            query_result.append(
                [age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex,
                 capital_gain,
                 capital_loss, hours_per_week, native_country, salary])

        session.close()
        #print(query_result)
        return query_result

