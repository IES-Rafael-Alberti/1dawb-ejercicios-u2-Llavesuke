import pytest
from src.ej22_4 import Countdown

@pytest.mark.parametrize(
    ('number, expected'),
    [
        (5,'5,4,3,2,1,0'),
        (12,'12,11,10,9,8,7,6,5,4,3,2,1,0')
    ]
)
def test_Countdown_params(number,expected):
    assert Countdown(number) == expected