from projekt.kalkulator import Kalkulator
from projekt.pamiec import Pamiec

def wpis(a, b, wybor, wynik):
    return {"a": a, "b": b, "op": wybor, "wynik": wynik}


def operacje():
    k = Kalkulator()
    pamiec = Pamiec("pamiec.json")
    operacje = {
        "+": k.dodawanie,
        "-": k.odejmowanie,
        "*": k.mnozenie,
        "/": k.dzielenie,
    }
    return operacje,pamiec

def main():

if __name__ == "__main__":
    main()