import pytest
from employee11_3 import Employee

@pytest.fixture
def employee():
    return Employee('eric', 'matthes', 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 75000
    