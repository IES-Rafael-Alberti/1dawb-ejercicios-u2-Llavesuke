import pytest
from src.ej2_05 import ask_salary, ask_age, verify

def test_ask_salary(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1000')
    result = ask_salary()
    assert result == 1000

def test_ask_age(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '12')
    result = ask_age()
    assert result == 12

@pytest.mark.parametrize(
    'age, salary, expected',
    [
        (12,1500,False),
        (16,900,False),
        (17,1800,True),
        (10,200,False)
    ]
)
def test_verify_params(age,salary,expected):
    assert verify(age,salary) == expected