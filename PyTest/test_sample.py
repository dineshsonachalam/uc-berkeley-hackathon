# pytest is a framework that makes building simple and scalable tests easy. Tests are expressive and readable—no
# boilerplate code required. Get started in minutes with a small unit test or complex functional test for your application or library.

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
    #  assert statement you're telling the program to test that condition,
    #  and trigger an error if the condition is false.

# Output: Command line
# C:\Users\Dinesh\Desktop\Python Testing\PyTest>pytest
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\PyTest, inifile:
# collected 1 item
#
# test_sample.py F
#
# ================================== FAILURES ===================================
# _________________________________ test_answer _________________________________
#
#     def test_answer():
# >       assert func(3) == 5
# E       assert 4 == 5
# E        +  where 4 = func(3)
#
# test_sample.py:9: AssertionError
# ========================== 1 failed in 0.09 seconds ===========================
#
# C:\Users\Dinesh\Desktop\Python Testing\PyTest>
