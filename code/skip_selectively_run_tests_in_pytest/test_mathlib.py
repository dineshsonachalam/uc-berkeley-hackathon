import mathlib
import pytest
@pytest.mark.skip(reason="I dont want to run this test at this moment")
def test_calc_total():
    total = mathlib.calc_total(5,6)
    assert total == 11

def test_cal_multiply():
    result = mathlib.calc_multiply(2,7)
    assert result == 14


#
# ===================== 1 passed, 1 skipped in 0.06 seconds =====================
#
# C:\Users\Dinesh\Desktop\Python Testing\code\skip_selectively_run_tests_in_pytest>pytest -v -rxs
# ============================= test session starts =============================
# platform win32 -- Python 3.6.3, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- C:\ProgramData\Anaconda3\python.exe
# cachedir: .cache
# rootdir: C:\Users\Dinesh\Desktop\Python Testing\code\skip_selectively_run_tests_in_pytest, inifile:
# plugins: flask-0.10.0
# collected 2 items
#
# test_mathlib.py::test_calc_total SKIPPED
# test_mathlib.py::test_cal_multiply PASSED
# =========================== short test summary info ===========================
# SKIP [1] test_mathlib.py:3: I dont want to run this test at this moment
#
# ===================== 1 passed, 1 skipped in 0.06 seconds =====================
#
# C:\Users\Dinesh\Desktop\Python Testing\code\skip_selectively_run_tests_in_pytest>
