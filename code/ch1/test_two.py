def test_failing():
    assert (1, 2, 3) == (3, 2, 1) # assert condition is false so triggers an error.


# Testing the function by: pytest test_two.py
# C:\Users\Dinesh\Desktop\Python Testing\code\ch1>pytest test_two.py
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\code\ch1, inifile:
# collected 1 item
#
# test_two.py F
#
# ================================== FAILURES ===================================
# ________________________________ test_failing _________________________________
#
#     def test_failing():
# >       assert (1, 2, 3) == (3, 2, 1) # assert condition is false so triggers an error.
# E       assert (1, 2, 3) == (3, 2, 1)
# E         At index 0 diff: 1 != 3
# E         Use -v to get the full diff
#
# test_two.py:2: AssertionError
# ========================== 1 failed in 0.22 seconds ===========================
#
# C:\Users\Dinesh\Desktop\Python Testing\code\ch1>    
