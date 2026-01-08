from typing import Protocol

class Operacje(Protocol):
    symbol = str
    name = str

    def wykonanie(self, a:float ,b:float ) -> float: ...


class Dodawanie:
    symbol = "+"
    name = "dodawanie"

    def wykonanie(self, a: float, b: float) -> float:
        return a + b

class Odjmowanie:
    symbol = "-"
    name = "odjmowanie"

    def wykonanie(self, a: float, b: float) -> float:
        return a - b

class Mnozenie:
    symbol = "*"
    name = "mnozenie"

    def wykonanie(self, a: float, b: float) -> float:
        return a * b

class Dzielenie:
    symbol = "/"
    name = "dzielenie"

    def wykonanie(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Nie mozna dzielic przez zero")
        return a / b

def pobierz_operacje() -> list[Operacje]:
    return [Dodawanie(),Odjmowanie(),Mnozenie(),Dzielenie()]
