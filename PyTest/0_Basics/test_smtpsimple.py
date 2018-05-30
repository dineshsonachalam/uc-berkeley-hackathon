# Fixture functions are registered by marking them with @pytest.fixture.
#  Let’s look at a simple
# self-contained test module containing a fixture and a test function using it:
import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0 # for demo purposes
