import sys
from flask import Blueprint, request, jsonify
sys.path.append("..")
from utility.crud import get_male_count, get_female_count, get_relationship_stats, get_adult_data

# Creating a blueprint class
adult_stats_blueprint = Blueprint('adult_stats',__name__,template_folder='templates')

@adult_stats_blueprint.route('/gender/stats',methods=['GET'])
def gender_stats():
    if request.method == 'GET':
        male_count = get_male_count()
        female_count = get_female_count()
        gender_stats = [
            {
                "gender" : 'Males',
                "value" : male_count,
            },
            {
                "gender" : 'Females',
                "value" : female_count,
            }
        ]
        return jsonify(gender_stats)

@adult_stats_blueprint.route('/relationship/stats',methods=['GET'])
def relationship_stats():
    if request.method == 'GET':
        wife_count,own_child_count,husband_count, \
        not_in_family_count, other_relative_count,unmarried_count = get_relationship_stats()
        gender_stats = [
            {
                "relationship" : 'Wife',
                "value" : wife_count
            },
            {
                "relationship" : 'Own-child',
                "value" : own_child_count
            },
            {
                "relationship" : 'Husband',
                "value" : husband_count
            },
            {
                "relationship" : 'Not-in-family',
                "value" : not_in_family_count
            },
            {
                "relationship" : 'Other-relative',
                "value" : other_relative_count
            },
            {
                "relationship" : 'Unmarried',
                "value" : unmarried_count
            }
        ]
        return jsonify(gender_stats)

@adult_stats_blueprint.route('/adult/stats',methods=['GET'])
def adult_data():
    if request.method == 'GET':
        data = get_adult_data()
        return jsonify(data)