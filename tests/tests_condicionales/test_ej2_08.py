import pytest
from src.condicionales.ej2_08 import Score, Level

def test_Score(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0.2)
    result = Score()
    assert result == 0.2

@pytest.mark.parametrize(
    'score, expected',
    [
        (0.0,'inaceptable'),
        (0.4,'aceptable'),
        (0.6,'meritorio'),
        (0.8,'meritorio')
    ]
)
def test_Level_params(score, expected):
    assert Level(score) == expected