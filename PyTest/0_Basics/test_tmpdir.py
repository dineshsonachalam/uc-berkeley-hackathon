# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0
# List the name tmpdir in the test function signature and pytest will lookup and
# call a fixture factory to create the resource before performing the test function call. Before
# the test runs, pytest creates a unique-per-test-invocation temporary directory:

# C:\Users\Dinesh\Desktop\Python Testing\PyTest>pytest -q test_tmpdir.py
# F
# ================================== FAILURES ===================================
# _______________________________ test_needsfiles _______________________________
#
# tmpdir = local('C:\\Users\\Dinesh\\AppData\\Local\\Temp\\pytest-of-Dinesh\\pytest-1\\test_needsfiles0')
#
#     def test_needsfiles(tmpdir):
#         print (tmpdir)
# >       assert 0
# E       assert 0
#
# test_tmpdir.py:4: AssertionError
# ---------------------------- Captured stdout call -----------------------------
# C:\Users\Dinesh\AppData\Local\Temp\pytest-of-Dinesh\pytest-1\test_needsfiles0
# 1 failed in 0.09 seconds
