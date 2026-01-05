import json
import pytest
from projekt.pamiec import Pamiec

p = Pamiec()

def test_inicjalizajca_bez_pliku(tmp_path):
    sciezka = tmp_path / "tesotwanie.json"

def test_odczyt():
    with  pytest.raises(FileNotFoundError, match=""):
        p.odczyt()

