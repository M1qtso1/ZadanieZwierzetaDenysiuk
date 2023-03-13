class Zwierzeta: # tworzenie klasy ze wszystkimi obiektami dla wszystkich klasow
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja):
        self.Gromada = Gromada
        self.Nazwa = Nazwa
        self.Kolor = Kolor
        self.IleZyja = IleZyja

    def show(self): # tworzenie funkcji wyswietlenia danych
        pass

class Ptak(Zwierzeta):# tworzenie klasy "Ptak" z wartosciami klasy "Zwierzeta" i unikalnymi wartosciami dla obiektow klasy "Ptak"
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, DlugoscDzioba, RozpietoscSkrzydel):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.DlugoscDzioba = DlugoscDzioba
        self.RozpietoscSkrzydel = RozpietoscSkrzydel
    def show(self): # tworzenie funkcji wyswietlenia danych
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"Dlugosc dzioba: {self.DlugoscDzioba}")
        print(f"RozpietoscSkrzydel: {self.RozpietoscSkrzydel}\n")

class Ssaki(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, GdzieZwykleMieszkaja):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.GdzieZwykleMieszkaja = GdzieZwykleMieszkaja
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"Zwykle mieszkaja w {self.GdzieZwykleMieszkaja}\n")

class Slimaki(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, MaMuszle):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.MaMuszle = MaMuszle
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"{self.MaMuszle} muszle\n")

class Gady(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, Dlugosc):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.Dlugosc = Dlugosc
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"Dlugosc: {self.Dlugosc}\n")

class Plazy(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, Trujaca):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.Trujaca = Trujaca
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"Trujaca: {self.Trujaca}\n")

class Owady(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, Masa):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.Masa = Masa
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"Masa: {self.Masa}\n")

class Promieniopletwe(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, JeInnych):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.JeInnych = JeInnych
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"{self.JeInnych} innych\n")

class RybyChrzestnoszkieletowe(Zwierzeta):
    def __init__(self, Gromada, Nazwa, Kolor, IleZyja, MaNogi):
        super().__init__(Gromada, Nazwa, Kolor, IleZyja)
        self.MaNogi = MaNogi
    def show(self):
        print(f"Gromada: {self.Gromada}")
        print(f"Nazwa: {self.Nazwa}")
        print(f"Kolor: {self.Kolor}")
        print(f"Zyja {self.IleZyja} lat")
        print(f"{self.MaNogi} nogi\n")

Kanarek = Ptak("Ptak", "Kanarek", "Zolty", "5-6", "2-3 cm", "20-30 cm") #dane elementu
Kanarek.show() #wyswietlenie elementu

Lew = Ssaki("Ssaki", "Lew", "Zolty", "25-40", "Central ZOO from Madagaskar")
Lew.show()

Orzel = Ptak("Ptak", "Orzel", "Bialy", "7-10", "12-15 cm", "120-150 cm")
Orzel.show()

Sojka = Ptak("Ptak", "Sojka", "Szary", "3-6", "1-2 cm", "15-20 cm")
Sojka.show()

Slimak = Slimaki("Slimaki", "Slimak", "Brazowy", "2-4", "Ma")
Slimak.show()

Wazboa = Gady("Gady", "Wazboa", "Czarny", "1-2", "70-80 cm")
Wazboa.show()

Antylopa = Ssaki("Ssaki", "Antylopa", "Brazowy", "3-5", "Afryce")
Antylopa.show()

Zaba = Plazy("Plazy", "Zaba", "Zielony", "1-2", "Nie")
Zaba.show()

Chrzaszcz = Owady("Owady", "Chrzaszcz", "Zielony", "0.1-0.5", "100 gr")
Chrzaszcz.show()

Modliszka = Owady("Owady", "Modliszka", "Zielony", "0.1-0.5", "100 gr")
Modliszka.show()

Sum = Promieniopletwe("Promieniopletwe", "Sum", "Szary","3-6", "Tak")
Sum.show()

Rekin = RybyChrzestnoszkieletowe("RybyChrzestnoszkieletowe", "Rekin", "Szary", "10-15", "Nie ma")
Rekin.show()
