"""Test for expected exceptions from using the API wrong."""

import pytest
import tasks # Importing every python file under tasks package

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/1 # here no error occurs -> FAILED

def test_working_on_assert():
    assert (1,2) == (1,2) # assert condition true -> PASSED

def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object') # here error occurs -> PASSED
        # here tasks must be a task object.

@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):  # owner must be string or none
        tasks.list_tasks(owner=123) # here error occurs -> PASSED
        # here owner must be a string


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError): # id must be an int
        tasks.get(task_id='123') # here error occurs since id = 'string' -> PASSED


class TestUpdate():
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


def test_delete_raises():
    """delete() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

if __name__ == '__main__':
    print("Type of tasks:",type(tasks)) #<class 'module'>
    print("tasks:",tasks)
    #  <module 'tasks' from 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\tasks\\__init__.py'>
    # tasks.add(task='not a Task object')
# TypeError: task must be Task object
