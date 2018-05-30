
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# Execute the test function with “quiet” reporting mode:
#
# $ pytest -q test_sysexit.py
# .                                                                    [100%]
# 1 passed in 0.12 seconds        
