import pytest
from src.ej22_6 import Piramide

@pytest.mark.parametrize(
    ('number, expected'),
    [
        (3,'*\n**\n***\n'),
        (5,'*\n**\n***\n****\n*****\n')
    ]
)
def test_Piramide_params(number,expected):
    assert Piramide(number) == expected