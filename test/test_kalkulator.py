import pytest
from projekt.kalkulator import Kalkulator

k = Kalkulator()


def test_dodawanie():
    assert k.dodawanie(2,3) == 5

def test_odejmowanie():
    assert k.odejmowanie(10, 5) == 5

def test_mnozenie():
    assert k.mnozenie(2,3) == 6

def test_dzielenie():
    assert k.dzielenie(10,2) == 5

def test_dzielenie_przez_zero():
    with pytest.raises(ValueError, match="nie dziel przez zero"):
        k.dzielenie(5,0 )