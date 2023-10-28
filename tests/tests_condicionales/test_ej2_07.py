import pytest
from src.condicionales.ej2_07 import UserRent, SelectPercentage

def test_UserRent(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10000')
    result = UserRent()
    assert result == 10000


@pytest.mark.parametrize(
    'rent, expected',
    [
        (3000,5),
        (12000,15),
        (26000,20),
        (43000,30),
        (62000,45)
    ]
)
def test_SelectPercentage_params(rent,expected):
    assert SelectPercentage(rent) == expected