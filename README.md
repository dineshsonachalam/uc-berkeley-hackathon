# Python Testing Tutorial

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

## Contributors

Dinesh Sonachalam
