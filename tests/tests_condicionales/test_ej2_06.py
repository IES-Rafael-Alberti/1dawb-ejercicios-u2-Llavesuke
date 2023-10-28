import pytest
from src.condicionales.ej2_06 import AskName, AskSex, AssignGroup

def test_AskName(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Anita')
    result = AskName()
    assert result == 'A'

def test_AskSex(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'M')   
    result = AskSex()
    assert result == 'M'

@pytest.mark.parametrize(
    'name, sex, expected',
    [
        ('A','M',False),
        ('O','M',True),
        ('A','F',True),
        ('N','M',True),
        ('A','M',False)
    ]
)
def test_AssignGroup_params(name,sex,expected):
    assert AssignGroup (name,sex) == expected