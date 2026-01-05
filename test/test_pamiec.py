import json
import pytest
from projekt.pamiec import Pamiec


def test_inicjalizajca_bez_pliku(tmp_path):
    sciezka = tmp_path / "tesotwanie.json"

    p = Pamiec(sciezka)

    assert p.dane == []

def test_zapis_do_pliku(tmp_path):
    sciezka = tmp_path / "testowanie.json"
    sciezka.write_text(json.dumps([{"a": 12.0, "b": 13.0, "op": "+", "wynik": 25.0}]))

    p = Pamiec(sciezka)

    assert p.dane == [{"a": 12.0, "b": 13.0, "op": "+", "wynik": 25.0}]

def test_odczyt_uszkodzonego_json(tmp_path):
    sciezka = tmp_path / "testowanie.json"
    sciezka.write_text("{niepoprawny json", encoding="utf-8")

    p = Pamiec(sciezka)

    assert p.dane == []

def test_zapis_dopisuje_do_listy_w_pamieci(tmp_path):
    sciezka = tmp_path / "testowanie.json"

    p = Pamiec(sciezka)
    p.zapis({"a": 1})
    p.zapis({"b": 2})

    assert p.dane == [{"a": 1}, {"b": 2}]

def test_zapis_pisze_do_pliku(tmp_path):
    sciezka = tmp_path / "testowanie.json"

    p = Pamiec(sciezka)
    p.zapis({"a": 1})
    zapisane = json.loads(sciezka.read_text(encoding="utf-8"))

    assert zapisane == [{"a": 1}]