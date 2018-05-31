from fixtures.mydb import MyDB # from fixtures package importing mydb.py

import pytest
 # Fixture functions are created by marking them with the @pytest.fixture decorator.
 # Test functions that require fixtures should accept them as arguments.

 # Fixtures have explicit names and are activated by declaring
 # them in test functions, modules, classes or whole projects
@pytest.fixture(scope="module") # calling pytest fixture module once
def cur():
    print("\n-----------------setting DB-------------------")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs # yields iterative
    # Return sends a specified value back to its caller
    # whereas Yield can produce a sequence of values.
    curs.close()
    conn.close()
    print("\n---------------------closing DB--------------------")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
