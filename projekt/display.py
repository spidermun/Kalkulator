
class Display():
    prompt = input("wybierz operacje: '+','-','*','/' ('q' aby wyjsc lub 'h' do oczytania historii): ")

    def show_menu(self, symbole: list[str]) -> str:
            print("---------------------")
            print("     KALKULATOR      ")
            print("---------------------")
            wybor = input(self.prompt.format(",".join(symbole)))
            print("---------------------")

    def ask_operands(self) -> tuple[float, float]:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        return a, b

    def show_result(self, wynik: float) -> None:
        print(f"Wynik = {wynik}")

    def show_history(self, historia: list[dict]) -> None:
        if not historia:
            print("Nie ma obecnie historii operacji. ")
        else:
            for h in historia:
                print(f"{h['a']} {h['op']} {h['b']} = {h['wynik']}")
                continue

    def show_error(self, wiadomosc: str) -> None:
        print(f"Blad: = {wiadomosc}")