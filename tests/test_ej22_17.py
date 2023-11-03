import pytest
from src.ej22_17 import User_Input

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1048')
    result = User_Input()
    assert result == '1048'