import pytest
from src.ej22_5 import Ask_User

def test_Ask_User(monkeypatch):
    inputs = iter([1500,5,3])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = Ask_User()
    assert result == (1500,5,3)