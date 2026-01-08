import json



class Pamiec:
    def __init__(self,sciezka):
        self.sciezka = sciezka
        self.dane = []
        self.odczyt()

    def odczyt(self):
        try:
            with open(self.sciezka,"r")as file:
                self.dane = json.load(file)
        except FileNotFoundError:
            self.dane = []
        except json.JSONDecodeError:
            self.dane = []

    def zapis(self, nowy_wpis):
        self.dane.append(nowy_wpis)
        try:
            with open(self.sciezka, "w") as file:
                json.dump(self.dane, file)
        except Exception as e:
            print(f"Błąd zapisu: {e}")
