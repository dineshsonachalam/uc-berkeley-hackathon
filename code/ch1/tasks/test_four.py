"""Test the Task data type."""
import pytest
from collections import namedtuple

# creating a named tuple called Task
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
# __new__.defaults to create Task object without having to specify all the field.

# one of the best way to mark the subset of your test function
@pytest.mark.run_these_all
def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21) # defining value in tuple
    t_dict = t_task._asdict() # converting tuple to dictionary {}
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected # two dictionaries are the same : True


def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    # underscore(_) in python indicates weakly private
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected # two tuples are the same

def test_initalization():
    tuple_1 = Task(summary='do something',owner='okken',done=True,id=21)
    #tuple_1 = Task(summary=None,owner=None,done=False,id=None)
    tuple_2 = Task() # Task(summary=None, owner=None, done=False, id=None)
    assert tuple_1 == tuple_2 # assert condition fails throws exception
    # assigning tuple object to tuple_1

def test_no_present_in_the_list():
    assert 1 in [2,3,4]
def test_character_lexicography_checker():
    assert 'a'<'b'
def test_Stringoperation():
    assert 'fizz' not in 'fizzbuzz'       
