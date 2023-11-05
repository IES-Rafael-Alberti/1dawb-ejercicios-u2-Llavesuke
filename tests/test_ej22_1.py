import pytest
from src.ej22_1 import User_input, Input_Loop

def test_User_Input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Perrazoboss')
    result = User_input()
    assert result == 'Perrazoboss'

@pytest.mark.parametrize(
    ('word, expected'),
    [
        ('naruto', (('naruto,'*9)+'naruto'))
    ]
)
def test_input_loop_params(word, expected):
    assert Input_Loop(word) == expected