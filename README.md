# Python Testing Tutorial

#### What is pytest?

A robust Python testing tool, pytest can be used for all types and levels of software testing. pytest
can be used by development teams, QA teams, independent testing groups, individuals practicing
TDD, and open source projects. In fact, projects all over the Internet have switched from unittest
or nose to pytest, including Mozilla and Dropbox. Why? Because pytest offers powerful features
such as ‘assert‘ rewriting, a third-party plugin model, and a powerful yet simple fixture model
that is unmatched in any other testing framework.
pytest is a software test framework, which means pytest is a command-line tool that
automatically finds tests you’ve written, runs the tests, and reports the results. It has a library of
goodies that you can use in your tests to help you test more effectively. It can be extended by
writing plugins or installing third-party plugins. It can be used to test Python distributions. And it
integrates easily with other tools like continuous integration and web automation.
Here are a few of the reasons pytest stands out above many other test frameworks:

* Simple tests are simple to write in pytest.
* Complex tests are still simple to write.
* Tests are easy to read.
* Tests are easy to read. (So important it’s listed twice.)
* You can get started in seconds.
* You use assert to fail a test, not things like self.assertEqual() or self.assertLessThan(). Just

assert.

* You can use pytest to run tests written for unittest or nose.

pytest is being actively developed and maintained by a passionate and growing community. It’s
so extensible and flexible that it will easily fit into your work flow. And because it’s installed
separately from your Python version, you can use the same latest version of pytest on legacy
Python 2 (2.6 and above) and Python 3 (3.3 and above).

####Test Strategy

While pytest is useful for unit testing, integration testing, system or end-to-end testing, and
functional testing, the strategy for testing the Tasks project focuses primarily on subcutaneous
functional testing. Following are some helpful definitions:

* Unit test: A test that checks a small bit of code, like a function or a class, in isolation of the

rest of the system. I consider the tests in Chapter 1, Getting Started with pytest , to be unit
tests run against the Tasks data structure.

* Integration test: A test that checks a larger bit of the code, maybe several classes, or a

subsystem. Mostly it’s a label used for some test larger than a unit test, but smaller than a
system test.
System test (end-to-end): A test that checks all of the system under test in an environment
as close to the end-user environment as possible.

* Functional test: A test that checks a single bit of functionality of a system. A test that

checks how well we add or delete or update a task item in Tasks is a functional test.

* Subcutaneous test: A test that doesn’t run against the final end-user interface, but against

an interface just below the surface. Since most of the tests in this book test against the API
layer—not the CLI—they qualify as subcutaneous tests.



### pytest Basic Testing commands

* `pytest` will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

* `assert` statement you're telling the program to test that condition,and trigger an error if the condition is false. 

  ## Assert that a certain exception is raised

  Use the `raises` helper to assert that some code raises an exception:

  ```
  # content of test_sysexit.py
  import pytest
  def f():
      raise SystemExit(1)

  def test_mytest():
      with pytest.raises(SystemExit):
          f()

  ```

  Execute the test function with “quiet” reporting mode:

  ```python
  $ pytest -q test_sysexit.py
  .                                                                    [100%]
  1 passed in 0.12 seconds
  ```

## Group multiple tests in a class

Once you develop multiple tests, you may want to group them into a class. pytest makes it easy to create a class containing more than one test:

```
# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

```

`pytest` discovers all tests following its [Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery), so it finds both `test_`prefixed functions. There is no need to subclass anything. We can simply run the module by passing its filename:

```
$ pytest -q test_class.py
.F                                                                   [100%]
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________

self = <test_class.TestClass object at 0xdeadbeef>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, 'check')
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
1 failed, 1 passed in 0.12 seconds
```

```
pytest --fixtures   # shows builtin and custom fixtures

```

Note that this command omits fixtures with leading `_` unless the `-v` option is added.

## Calling pytest through `python -m pytest`

New in version 2.0.

You can invoke testing through the Python interpreter from the command line:

```
python -m pytest [...]

```

This is almost equivalent to invoking the command line script `pytest [...]` directly, except that calling via `python` will also add the current directory to `sys.path`.

**-m MARKEXPR:**

Markers: one of the best ways to mark the subsets of your test function.

For Example: One way to run test_passing() and test_asdict()  is to mark them in separate files.

Now in this repository code/ch1

In test_one.py :

```python
import pytest
@pytest.mark.run_these_all
def test_passing():

	assert (1, 2, 3) == (1,2,3)


```

In test_four.py

```python
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


```



```
C:\Users\Dinesh\Desktop\Python Testing\code\ch1>pytest -v -m run_these_all
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- C:\ProgramData\Anaconda3\python.exe
cachedir: .cache
rootdir: C:\Users\Dinesh\Desktop\Python Testing\code\ch1, inifile:
collected 7 items

test_one.py::test_passing PASSED
tasks/test_four.py::test_asdict PASSED

============================= 5 tests deselected ==============================
=================== 2 passed, 5 deselected in 0.07 seconds ====================
```



## Contributors

Dinesh Sonachalam
