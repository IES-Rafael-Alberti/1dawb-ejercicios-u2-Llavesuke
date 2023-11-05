import pytest
from src.ej22_11 import Wordbyword

@pytest.mark.parametrize(
    ('word, expected'),
    [
        ('Naruto','\no\nt\nu\nr\na\nN '),
        ('Perrito bueno', '\no\nn\ne\nu\nb\n \no\nt\ni\nr\nr\ne\nP ')
    ]
)
def test_Wordbyword_params(word,expected):
    assert Wordbyword(word) == expected