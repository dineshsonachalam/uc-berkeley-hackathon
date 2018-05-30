"""Test the Task data type."""
# tuples are immutable whereas lists are mutable.
# tuple use () whereas lists uses [].

# namedtuple is a factory function for making a tuple class. With that class
# we can create tuples that are callable by name also.
from collections import namedtuple

# The Tasks project uses a structure called Task, which is
# based on the namedtuple factory method, which is part of the standard library.
# The Task structure is used as a data structure to pass information between
# the UI and the API.


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
# __new__.defaults to create Task object without having to specify all the field.



def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task() # Invokes defaults
    t2 = Task(None, None, False, None)
    assert t1 == t2 # Assert condition True


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')  # assigning first two values
    # Now here t.summary = 'buy milk'
    # Now here t.owner = 'brian'

    assert t.summary == 'buy milk' # index[0] == summary -> True
    assert t.owner == 'brian' # index[1] == owner -> True
    assert (t.done, t.id) == (False, None)

if __name__ == "__main__":
    t1=Task()
    print(type(t1)) # <class '__main__.Task'>
    print(type(t1.done)) # <class 'bool'>
    print("T1------------->",t1) # Task(summary=None, owner=None, done=False, id=None)
    print(t1.summary) #None
    print(t1.owner) #None
    print(t1.done) #False
    print(t1.id) #None
    t2 = Task(False,False,None,False)
    print("T2------------>",t2) # Task(summary=False, owner=False, done=None, id=False)
    t = Task('buy milk', 'brian')  # assigning first two values
    print(t.summary) # buy milk
