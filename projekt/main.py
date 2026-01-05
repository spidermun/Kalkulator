from projekt.kalkulator import Kalkulator
from pamiec import Pamiec

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
    op, pamiec = operacje()
    while True:
        print("---------------------")
        print("     KALKULATOR      ")
        print("---------------------")
        wybor = input("wybierz operacje: '+','-','*','/' ('q' aby wyjsc lub 'h' do oczytania historii): ")
        print("---------------------")

        if wybor == "q":
            break

        elif wybor == "h":
            if pamiec.dane == []:
                print("puste")
            else:
                for h in pamiec.dane:
                    print(f"{h['a']} {h['op']} {h['b']} = {h['wynik']}")
            continue

        elif wybor not in op:
            print("nie prawidlowy operator")
            continue


        try:
            a = float(input("Podaj a: "))
            b = float(input("Podaj b: "))
            wynik = op[wybor](a, b)

        except ValueError as e:
            print(f"Blad: {e}")
            continue

        pamiec.zapis(wpis(a, b, wybor, wynik))
        print(f"Wynik = {wynik}")


if __name__ == "__main__":
    main()