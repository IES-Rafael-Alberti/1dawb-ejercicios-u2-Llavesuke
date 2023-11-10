import pytest
from src.ej22_2 import Age_Sucesion

@pytest.mark.parametrize(
    ('age, expected'),
    [
        (5,'0,1,2,3,4,5'),
        (12,'0,1,2,3,4,5,6,7,8,9,10,11,12')
    ]
)
def test_age_sucesion_params(age,expected):
    assert Age_Sucesion(age) == expected