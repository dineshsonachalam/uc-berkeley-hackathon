from flask import Blueprint,request, jsonify, render_template, session,Markup,redirect,Flask
from utility.sqlalchemy_orm import Adult
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime
from sqlalchemy.orm import sessionmaker
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
# Use already created database
engine = create_engine('sqlite:///adult_dataset.db', echo=False)
Base = declarative_base()

# Creating columns
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

# Creating a blueprint class
adult_statistics_blueprint = Blueprint('adult_statistics',__name__,template_folder='templates')

# Creating an object of class Adult from utility/sqlachemy_orm.py
a = Adult(age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,
                 capital_loss,hours_per_week,native_country,salary)


@adult_statistics_blueprint.route('/',methods=['GET','POST'],endpoint='index')
def index():
    if request.method == 'GET':


        # Setting default values of sex,race,relationship as All values from their column category
        sex = request.args.get('sex', default='Male,Female', type=str)
        sex = sex.split(",") # Converting string to list seperated by ","
        #print("Sex_1:",sex)

        race = request.args.get('race', default='White,Asian-Pac-Islander,Amer-Indian-Eskimo,Other,Black', type=str)
        race = race.split(",")

        relationship = request.args.get('relationship', default='Wife,Own-child,Husband,Not-in-family,Other-relative,Unmarried',type=str)
        relationship = relationship.split(",")

        # Initialize an empty string
        html_table = ""

        # Query all from the Database
        if (sex == ['Male', 'Female'] and race==['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
                and relationship==['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']):
            c = cache.get('default-table')  # Cache for Table

            # If no cache present
            if c is None:

                print("No cache present, directly hitting the database.")
                query_result = a.query_all()  # Calling query_all() from Adult Class present in utility/sqlalchemy_orm.py
                count = 1 # For serial no in HTML Table -> Iterating it by 1
                # html_table : Initializing HTML Table as a Python String
                html_table = """<table class="table">
                                  <thead>
                                    <tr>
                                      <th scope="col">S.no</th> 
                                      <th scope="col">Age</th> 
                                      <th scope="col">Workclass</th> 
                                      <th scope="col">fnlwgt</th> 
                                      <th scope="col">education</th> 
                                      <th scope="col">education num</th> 
                                      <th scope="col">marital status</th> 
                                      <th scope="col">occupation</th>       
                                      <th scope="col">Relationship</th> 
                                      <th scope="col">Race</th> 
                                      <th scope="col">Sex</th> 
                                      <th scope="col">Capital gain</th> 
                                      <th scope="col">Capital loss</th> 
                                      <th scope="col">Hours per week</th> 
                                      <th scope="col">Native Country</th> 
                                      <th scope="col">Salary</th> 
                                    </tr>
                                  </thead>
                                  <tbody>"""
                # Setting table data values from query_result list
                for i in range(0, len(query_result)):
                    html_table = html_table + """ <tr> <th scope="row">  """ + str(count) + """</th>"""
                    html_table = html_table + """<td>""" + str(query_result[i][0]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][1]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][2]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][3]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][4]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][5]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][6]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][7]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][8]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][9]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][10]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][11]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][12]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][13]) + """</td>"""
                    html_table = html_table + """<td>""" + str(query_result[i][14]) + """</td>"""
                    html_table = html_table + """</tr>"""
                    count = count + 1

                html_table = html_table + """  </tbody>
                        </table>"""
                cache.set('default-table', html_table, timeout=5 * 60) # setting the cache
            else:
                # If cache is not none using existing cache
                print("Using Table Cache")
                html_table = c
        else:
            # If a filter condition is used from the drop down.
            # A filtered table is loaded
            print("Using Filter Condition")
            query_result = a.query_filter(sex, race, relationship)  # calling query_filter of Adult class
            count = 1
            html_table = """<table class="table">
                                              <thead>
                                                <tr>
                                                  <th scope="col">S.no</th> 
                                                  <th scope="col">Age</th> 
                                                  <th scope="col">Workclass</th> 
                                                  <th scope="col">fnlwgt</th> 
                                                  <th scope="col">education</th> 
                                                  <th scope="col">education num</th> 
                                                  <th scope="col">marital status</th> 
                                                  <th scope="col">occupation</th>       
                                                  <th scope="col">Relationship</th> 
                                                  <th scope="col">Race</th> 
                                                  <th scope="col">Sex</th> 
                                                  <th scope="col">Capital gain</th> 
                                                  <th scope="col">Capital loss</th> 
                                                  <th scope="col">Hours per week</th> 
                                                  <th scope="col">Native Country</th> 
                                                  <th scope="col">Salary</th> 
                                                </tr>
                                              </thead>
                                              <tbody>"""
            for i in range(0, len(query_result)):
                html_table = html_table + """ <tr> <th scope="row">  """ + str(count) + """</th>"""
                html_table = html_table + """<td>""" + str(query_result[i][0]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][1]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][2]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][3]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][4]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][5]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][6]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][7]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][8]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][9]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][10]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][11]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][12]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][13]) + """</td>"""
                html_table = html_table + """<td>""" + str(query_result[i][14]) + """</td>"""
                html_table = html_table + """</tr>"""
                count = count + 1

            html_table = html_table + """  </tbody>
                                    </table>"""

        g1 = cache.get('default-graph-1')  # Cache for graph 1
        g2 = cache.get('default-graph-2')  # Cache for graph 2
        if g1 is None:
            # If graph 1 cache is none
            gender_count = a.total_males_females() # A list returned that contains total number of males and females
            cache.set('default-graph-1',gender_count, timeout=5 * 60)
        else:
            # Using Graph 1 cache
            gender_count = g1
            print("Using Graph 1 Cache")

        if g2 is None:
            relationship_count = a.total_people_in_relationship() # A list returned that contains total number of people in each relationship
            cache.set('default-graph-2',relationship_count, timeout=5 * 60)
        else:
            relationship_count = g2
            print("Using Graph 2 Cache")

        male_count = gender_count[0]
        female_count = gender_count[1]

        Wife_count = relationship_count[0]
        Own_child_count = relationship_count[1]
        Husband_count = relationship_count[2]
        Not_in_family_count = relationship_count[3]
        Other_relative_count = relationship_count[4]
        Unmarried_count = relationship_count[5]



        # print("Table Update:",query_result)
        # print("--------------------------------------------------")
        # print("Male Count:",male_count)
        # print("female Count:",female_count)
        # print("--------------------------------------------------")
        # print("Wife_count:",Wife_count)
        # print("Own_child_count:",Own_child_count)
        # print("Husband_count:",Husband_count)
        # print("Not_in_family_count:",Not_in_family_count)
        # print("Other_relative_count:",Other_relative_count)
        # print("Unmarried_count:",Unmarried_count)


        return render_template('index.html',male_count=male_count,female_count=female_count,
                               Wife_count=Wife_count,Own_child_count=Own_child_count,Husband_count=Husband_count,
                               Not_in_family_count=Not_in_family_count,Other_relative_count=Other_relative_count,
                               Unmarried_count=Unmarried_count,html_table = Markup(html_table))
    elif request.method == 'POST':
        return redirect('/')








