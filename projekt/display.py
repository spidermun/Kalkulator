class Display:
    def menu(self, symbole: list[str]) -> str:
        print("---------------------")
        print("     KALKULATOR      ")
        print("---------------------")
        prompt = f"wybierz operacje: {', '.join(symbole)} ('q' aby wyjsc, 'h' historia): "
        wybor = input(prompt)
        print("---------------------")
        return wybor

    def operatory(self) -> tuple[float, float]:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        return a, b

    def wynik(self, wynik: float) -> None:
        print(f"Wynik = {wynik}")

    def historia(self, historia: list[dict]) -> None:
        if not historia:
            print("Nie ma obecnie historii operacji.")
        else:
            for h in historia:
                print(f"{h['a']} {h['op']} {h['b']} = {h['wynik']}")

    def blad(self, wiadomosc: str) -> None:
        print(f"Blad: {wiadomosc}")