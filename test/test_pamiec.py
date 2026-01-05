import json
import pytest
from projekt.pamiec import Pamiec


def test_inicjalizajca_bez_pliku(tmp_path):
    sciezka = tmp_path / "tesotwanie.json"
    p = Pamiec(sciezka)
    assert p.dane == []

