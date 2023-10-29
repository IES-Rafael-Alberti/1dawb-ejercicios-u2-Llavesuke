import pytest
from src.ej22_1 import User_Input, Input_Loop

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Perrazoboss')
    result = User_Input()
    assert result == 'Perrazoboss'

@pytest.mark.parametrize(
    'imported_input, expected',
    [
        ('Naruto,','Naruto,'*9+'Naruto')
    ]
)
def test_Input_Loop_params(imported_input,expected):
    assert Input_Loop(imported_input) == expected