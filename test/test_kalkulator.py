from projekt.kalkulator import Kalkulator

def test_dodawanie():
    k = Kalkulator()
    assert k.dodawanie(2,3) == 5