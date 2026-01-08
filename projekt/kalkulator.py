
from projekt.operacje import pobierz_operacje, Operacje

class Kalkulator:
    def __init__(self) -> None:
        self._operacje: dict[str, Operacje] = {op.symbol: op for op in pobierz_operacje()}

    def symbole(self) -> list[str]:
        return list(self._operacje.keys())

    def wykonaj(self, symbol: str, a: float, b: float) -> float:
        if symbol not in self._operacje:
            raise ValueError(f"Nieznana operacja: {symbol}")
        return self._operacje[symbol].wykonanie(a, b)