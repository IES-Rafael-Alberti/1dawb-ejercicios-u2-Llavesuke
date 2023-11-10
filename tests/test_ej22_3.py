import pytest
from src.ej22_3 import Impar

@pytest.mark.parametrize(
    ('number, expected'),
    [
        (5,'1,3,5'),
        (12,'1,3,5,7,9,11')
    ]
)
def test_Impar_params(number,expected):
    assert Impar(number) == expected