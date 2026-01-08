from projekt.kalkulator import Kalkulator
from projekt.pamiec import Pamiec
from projekt.display import Display

def wpis(a: float, b: float, wybor: str, wynik: float) -> dict:
    return {"a": a, "b": b, "op": wybor, "wynik": wynik}

def main():
    kalk = Kalkulator()
    pamiec = Pamiec("pamiec.json")
    ui = Display()

    while True:
        wybor = ui.menu(kalk.symbole())
        if wybor.lower() == "q":
            break
        if wybor.lower() == "h":
            ui.historia(pamiec.dane)
            continue

        try:
            a, b = ui.operatory()
            wynik = kalk.wykonaj(wybor, a, b)
            ui.wynik(wynik)
            pamiec.zapis(wpis(a, b, wybor, wynik))
        except ValueError as e:
            ui.blad(str(e))
        except Exception as e:
            ui.blad(f"Nieoczekiwany blad: {e}")

if __name__ == "__main__":
    main()