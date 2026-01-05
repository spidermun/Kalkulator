import json
import pytest
from projekt.pamiec import Pamiec


import json
from projekt.pamiec import Pamiec

def test_inicjalizajca_bez_pliku(tmp_path):
    sciezka = tmp_path / "testowanie.json"

    p = Pamiec(sciezka)

    assert p.dane == []

def test_zapis_do_pliku(tmp_path):
    sciezka = tmp_path / "testowanie.json"
    sciezka.write_text(json.dumps([{"a": 12.0, "b": 13.0, "op": "+", "wynik": 25.0}]))

    p = Pamiec(sciezka)

    assert p.dane == [{"a": 12.0, "b": 13.0, "op": "+", "wynik": 25.0}]

def test_odczyt_uszkodzonego_json(tmp_path):
    sciezka = tmp_path / "testowanie.json"
    sciezka.write_text("{niepoprawny json")

    p = Pamiec(sciezka)

    assert p.dane == []

def test_zapis_dopisuje_do_listy_w_pamieci(tmp_path):
    sciezka = tmp_path / "testowanie.json"

    p = Pamiec(sciezka)
    p.zapis({"a": 1.0, "b": 2.0, "op": "+", "wynik": 3.0})
    p.zapis({"a": 5.0, "b": 4.0, "op": "-", "wynik": 1.0})

    assert p.dane == [
        {"a": 1.0, "b": 2.0, "op": "+", "wynik": 3.0},
        {"a": 5.0, "b": 4.0, "op": "-", "wynik": 1.0},
    ]

def test_zapis_pisze_do_pliku(tmp_path):
    sciezka = tmp_path / "testowanie.json"

    p = Pamiec(sciezka)
    p.zapis({"a": 7.0, "b": 3.0, "op": "*", "wynik": 21.0})
    zapisane = json.loads(sciezka.read_text(encoding="utf-8"))

    assert zapisane == [{"a": 7.0, "b": 3.0, "op": "*", "wynik": 21.0}]