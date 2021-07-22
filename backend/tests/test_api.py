import requests

def test_gender_stats():
    url = "http://0.0.0.0:8002/gender/stats"
    response = requests.request("GET", url, headers={}, data={})
    assert response.status_code == 200
    response = response.json()
    expected_response = [
        {
            "gender": "Males",
            "value": 21790
        },
        {
            "gender": "Females",
            "value": 10771
        }
    ]
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))

def test_relationship_stats():
    url = "http://0.0.0.0:8002/relationship/stats"
    response = requests.request("GET", url, headers={}, data={})    
    assert response.status_code == 200
    response = response.json()
    expected_response = [
            {
                "relationship": "Wife",
                "value": 1568
            },
            {
                "relationship": "Own-child",
                "value": 5068
            },
            {
                "relationship": "Husband",
                "value": 13193
            },
            {
                "relationship": "Not-in-family",
                "value": 8305
            },
            {
                "relationship": "Other-relative",
                "value": 981
            },
            {
                "relationship": "Unmarried",
                "value": 3446
            }
        ]
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))

def test_adult_data():
    url = "http://0.0.0.0:8002/adult/stats"
    response = requests.request("GET", url, headers={}, data={})    
    assert response.status_code == 200
    response = response.json()
    expected_response = [
        {
            "age": "39",
            "education": "Bachelors",
            "id": 1,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "50",
            "education": "Bachelors",
            "id": 2,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "38",
            "education": "HS-grad",
            "id": 3,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "53",
            "education": "11th",
            "id": 4,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "28",
            "education": "Bachelors",
            "id": 5,
            "marital_status": "Married-civ-spouse",
            "native_country": "Cuba",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "37",
            "education": "Masters",
            "id": 6,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "49",
            "education": "9th",
            "id": 7,
            "marital_status": "Married-spouse-absent",
            "native_country": "Jamaica",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "52",
            "education": "HS-grad",
            "id": 8,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "31",
            "education": "Masters",
            "id": 9,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "42",
            "education": "Bachelors",
            "id": 10,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "37",
            "education": "Some-college",
            "id": 11,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "30",
            "education": "Bachelors",
            "id": 12,
            "marital_status": "Married-civ-spouse",
            "native_country": "India",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "23",
            "education": "Bachelors",
            "id": 13,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "32",
            "education": "Assoc-acdm",
            "id": 14,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "40",
            "education": "Assoc-voc",
            "id": 15,
            "marital_status": "Married-civ-spouse",
            "native_country": "?",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "34",
            "education": "7th-8th",
            "id": 16,
            "marital_status": "Married-civ-spouse",
            "native_country": "Mexico",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "25",
            "education": "HS-grad",
            "id": 17,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "32",
            "education": "HS-grad",
            "id": 18,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "38",
            "education": "11th",
            "id": 19,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "43",
            "education": "Masters",
            "id": 20,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "40",
            "education": "Doctorate",
            "id": 21,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "54",
            "education": "HS-grad",
            "id": 22,
            "marital_status": "Separated",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "35",
            "education": "9th",
            "id": 23,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "43",
            "education": "11th",
            "id": 24,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "59",
            "education": "HS-grad",
            "id": 25,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "56",
            "education": "Bachelors",
            "id": 26,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "19",
            "education": "HS-grad",
            "id": 27,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "54",
            "education": "Some-college",
            "id": 28,
            "marital_status": "Married-civ-spouse",
            "native_country": "South",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "39",
            "education": "HS-grad",
            "id": 29,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "49",
            "education": "HS-grad",
            "id": 30,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "23",
            "education": "Assoc-acdm",
            "id": 31,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "20",
            "education": "Some-college",
            "id": 32,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "45",
            "education": "Bachelors",
            "id": 33,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "30",
            "education": "Some-college",
            "id": 34,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "22",
            "education": "Some-college",
            "id": 35,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "48",
            "education": "11th",
            "id": 36,
            "marital_status": "Never-married",
            "native_country": "Puerto-Rico",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "21",
            "education": "Some-college",
            "id": 37,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "19",
            "education": "HS-grad",
            "id": 38,
            "marital_status": "Married-AF-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "31",
            "education": "Some-college",
            "id": 39,
            "marital_status": "Married-civ-spouse",
            "native_country": "?",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "48",
            "education": "Assoc-acdm",
            "id": 40,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "31",
            "education": "9th",
            "id": 41,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "53",
            "education": "Bachelors",
            "id": 42,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "24",
            "education": "Bachelors",
            "id": 43,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "49",
            "education": "HS-grad",
            "id": 44,
            "marital_status": "Separated",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "25",
            "education": "HS-grad",
            "id": 45,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "57",
            "education": "Bachelors",
            "id": 46,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "53",
            "education": "HS-grad",
            "id": 47,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "44",
            "education": "Masters",
            "id": 48,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "41",
            "education": "Assoc-voc",
            "id": 49,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "29",
            "education": "Assoc-voc",
            "id": 50,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "25",
            "education": "Some-college",
            "id": 51,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "18",
            "education": "HS-grad",
            "id": 52,
            "marital_status": "Never-married",
            "native_country": "?",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "47",
            "education": "Prof-school",
            "id": 53,
            "marital_status": "Married-civ-spouse",
            "native_country": "Honduras",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "50",
            "education": "Bachelors",
            "id": 54,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "47",
            "education": "HS-grad",
            "id": 55,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "43",
            "education": "Some-college",
            "id": 56,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "46",
            "education": "5th-6th",
            "id": 57,
            "marital_status": "Married-civ-spouse",
            "native_country": "Mexico",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "35",
            "education": "Assoc-voc",
            "id": 58,
            "marital_status": "Married-civ-spouse",
            "native_country": "Puerto-Rico",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "41",
            "education": "HS-grad",
            "id": 59,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "30",
            "education": "HS-grad",
            "id": 60,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "30",
            "education": "Bachelors",
            "id": 61,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "32",
            "education": "7th-8th",
            "id": 62,
            "marital_status": "Married-spouse-absent",
            "native_country": "?",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "48",
            "education": "HS-grad",
            "id": 63,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "42",
            "education": "Doctorate",
            "id": 64,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "29",
            "education": "Some-college",
            "id": 65,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "36",
            "education": "HS-grad",
            "id": 66,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "28",
            "education": "Some-college",
            "id": 67,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "53",
            "education": "HS-grad",
            "id": 68,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "49",
            "education": "Some-college",
            "id": 69,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "25",
            "education": "Some-college",
            "id": 70,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "19",
            "education": "Some-college",
            "id": 71,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "31",
            "education": "Bachelors",
            "id": 72,
            "marital_status": "Separated",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "29",
            "education": "Bachelors",
            "id": 73,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "23",
            "education": "Some-college",
            "id": 74,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "79",
            "education": "Some-college",
            "id": 75,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "27",
            "education": "HS-grad",
            "id": 76,
            "marital_status": "Never-married",
            "native_country": "Mexico",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "40",
            "education": "Assoc-acdm",
            "id": 77,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "67",
            "education": "10th",
            "id": 78,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "18",
            "education": "11th",
            "id": 79,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "31",
            "education": "7th-8th",
            "id": 80,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "18",
            "education": "HS-grad",
            "id": 81,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "52",
            "education": "Bachelors",
            "id": 82,
            "marital_status": "Married-civ-spouse",
            "native_country": "Cuba",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "46",
            "education": "HS-grad",
            "id": 83,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "59",
            "education": "HS-grad",
            "id": 84,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "44",
            "education": "HS-grad",
            "id": 85,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "53",
            "education": "HS-grad",
            "id": 86,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "49",
            "education": "HS-grad",
            "id": 87,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "33",
            "education": "Masters",
            "id": 88,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "30",
            "education": "9th",
            "id": 89,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "43",
            "education": "Doctorate",
            "id": 90,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Female"
        },
        {
            "age": "57",
            "education": "Assoc-voc",
            "id": 91,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "37",
            "education": "Some-college",
            "id": 92,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "28",
            "education": "Some-college",
            "id": 93,
            "marital_status": "Divorced",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "30",
            "education": "HS-grad",
            "id": 94,
            "marital_status": "Married-civ-spouse",
            "native_country": "?",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "34",
            "education": "Bachelors",
            "id": 95,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "29",
            "education": "Some-college",
            "id": 96,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        },
        {
            "age": "48",
            "education": "Doctorate",
            "id": 97,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "37",
            "education": "Some-college",
            "id": 98,
            "marital_status": "Married-civ-spouse",
            "native_country": "United-States",
            "salary": ">50K",
            "sex": "Male"
        },
        {
            "age": "48",
            "education": "Assoc-acdm",
            "id": 99,
            "marital_status": "Divorced",
            "native_country": "England",
            "salary": "<=50K",
            "sex": "Female"
        },
        {
            "age": "32",
            "education": "HS-grad",
            "id": 100,
            "marital_status": "Never-married",
            "native_country": "United-States",
            "salary": "<=50K",
            "sex": "Male"
        }
    ]
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))
