import pytest
from src.ej22_1 import PedirNumeros, Input_Loop

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Perrazoboss')
    result = PedirNumeros()
    assert result == 'Perrazoboss'
