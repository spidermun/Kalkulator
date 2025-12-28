class Kalkulator:
    def __init__(self):
        pass

    def dodawanie(self, a: float, b: float) -> float:
        return a + b

    def odejmowanie(self, a: float, b: float) -> float:
        return a - b

    def mnozenie(self, a: float, b: float) -> float:
        return a * b

    def dzielenie(self, a: float, b: float) -> float:
        if b == 0:
            raise  ValueError("nie dziel przez zero jasna ch...")
        return a / b
