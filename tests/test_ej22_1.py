import pytest
from src.ej22_1 import User_Input, Input_Loop

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Perrazoboss')
    result = User_Input()
    assert result == 'Perrazoboss'
