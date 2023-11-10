import pytest
from src.ej22_10 import Primo

@pytest.mark.parametrize(
    ('number, expected'),
    [
        (1,True),
        (4,False),
        (7,True)
    ]
)
def test_Primo_params(number,expected):
    assert Primo(number) == expected