import pytest
@pytest.mark.run_these_all
def test_passing():
    assert (1, 2, 3) == (1,2,3)
    # (assert condition)
    # youre telling the program to test that condition,
    # and trigger an error if the condition is false.

# If you need more info use -v or --verbose
#
# C:\Users\Dinesh\Desktop\Python Testing\code\ch1>pytest -v test_one.py
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- C:\ProgramData\Anaconda3\python.exe
# cachedir: .cache
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\code\ch1, inifile:
# collected 1 item
#
# test_one.py::test_passing PASSED






# C:\Users\Dinesh\Desktop\Python Testing\code\ch1>pytest test_one.py
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\code\ch1, inifile:
# collected 1 item
#
# test_one.py .
#
# ========================== 1 passed in 0.07 seconds ===========================
#
