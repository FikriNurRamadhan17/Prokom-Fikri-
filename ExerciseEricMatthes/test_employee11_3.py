from employee11_3 import Employee

def test_give_default_raise():
    emp = Employee('eric', 'matthes', 65000)
    emp.give_raise()
    assert emp.annual_salary == 70000

def test_give_custom_raise():
    emp = Employee('eric', 'matthes', 65000)
    emp.give_raise(10000)
    assert emp.annual_salary == 75000
    