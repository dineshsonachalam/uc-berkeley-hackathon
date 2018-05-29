# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check') # has attribute
        
# C:\Users\Dinesh\Desktop\Python Testing\PyTest>pytest
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\PyTest, inifile:
# collected 4 items
#
# test_class.py .F
# test_sample.py F
# test_sysexit.py .
#
# ================================== FAILURES ===================================
# _____________________________ TestClass.test_two ______________________________
#
# self = <test_class.TestClass object at 0x000001F6DEEC4748>
#
#     def test_two(self):
#         x = "hello"
# >       assert hasattr(x, 'check') # has attribute
# E       AssertionError: assert False
# E        +  where False = hasattr('hello', 'check')
#
# test_class.py:9: AssertionError
# _________________________________ test_answer _________________________________
#
#     def test_answer():
# >       assert func(3) == 5
# E       assert 4 == 5
# E        +  where 4 = func(3)
#
# test_sample.py:9: AssertionError
# ===================== 2 failed, 2 passed in 0.13 seconds ======================
