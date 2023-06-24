import csv
class Pracownik:
    def __init__(self, imie, wiek, stanowisko):
        self.imie = imie
        self.wiek = wiek
        self.stanowisko = stanowisko
    def __str__(self):
        return f"Imię: {self.imie}, Wiek: {self.wiek}, Stanowisko: {self.stanowisko}"
class SystemZarzadzaniaKadrami:
    def __init__(self):
        self.pracownicy = []
    def dodaj_pracownika(self, imie, wiek, stanowisko):
        pracownik = Pracownik(imie, wiek, stanowisko)
        self.pracownicy.append(pracownik)
    def usun_pracownika(self, imie):
        for pracownik in self.pracownicy:
            if pracownik.imie == imie:
                self.pracownicy.remove(pracownik)
                return True
        return False
    def aktualizuj_pracownika(self, imie, nowe_imie=None, nowy_wiek=None, nowe_stanowisko=None):
        for pracownik in self.pracownicy:
            if pracownik.imie == imie:
                if nowe_imie:
                    pracownik.imie = nowe_imie
                if nowy_wiek:
                    pracownik.wiek = nowy_wiek
                if nowe_stanowisko:
                    pracownik.stanowisko = nowe_stanowisko
                return True
        return False
    def wyszukaj_pracownika(self, imie):
        for pracownik in self.pracownicy:
            if pracownik.imie == imie:
                return pracownik
        return None
    def lista_pracownikow(self):
        return self.pracownicy
    def pracownicy_po_stanowisku(self, stanowisko):
        pracownicy_filtr = []
        for pracownik in self.pracownicy:
            if pracownik.stanowisko == stanowisko:
                pracownicy_filtr.append(pracownik)
        return pracownicy_filtr
    def sredni_wiek_pracownikow(self):
        suma_wiekow = 0
        for pracownik in self.pracownicy:
            suma_wiekow += pracownik.wiek
        if len(self.pracownicy) > 0:
            sredni_wiek = suma_wiekow / len(self.pracownicy)
            return sredni_wiek
        else:
            return 0
    def zapisz_do_pliku_csv(self, nazwa_pliku):
        with open(nazwa_pliku, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Imię', 'Wiek', 'Stanowisko'])
            for pracownik in self.pracownicy:
                writer.writerow([pracownik.imie, pracownik.wiek, pracownik.stanowisko])
    def odczytaj_z_pliku_csv(self, nazwa_pliku):
        self.pracownicy = []
        with open(nazwa_pliku, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pomijanie nagłówka
            for row in reader:
                imie = row[0]
                wiek = int(row[1])
                stanowisko = row[2]
                self.dodaj_pracownika(imie, wiek, stanowisko)
system_kadrowy = SystemZarzadzaniaKadrami()

while True:
    print("Dodawanie pracownika:")
    imie = input("Podaj dane pracownika (lub wpisz 'q' aby zakończyć): ")
    if imie == 'q':
        break
    wiek = int(input("Podaj wiek pracownika: "))
    stanowisko = input("Podaj stanowisko pracownika: ")
    system_kadrowy.dodaj_pracownika(imie, wiek, stanowisko)
# Zapis danych do pliku CSV
system_kadrowy.zapisz_do_pliku_csv("pracownicy.csv")
# Usunięcie pracownika
system_kadrowy.usun_pracownika("Jan Kowalski")
# Wyświetlenie zaktualizowanej listy pracowników
lista_pracownikow = system_kadrowy.lista_pracownikow()
for pracownik in lista_pracownikow:
    print(pracownik)
# Aktualizacja informacji o pracowniku
system_kadrowy.aktualizuj_pracownika("Anna Nowak", nowe_imie="Anna Kowalczyk", nowy_wiek=26)
# Wyszukiwanie pracownika
pracownik = system_kadrowy.wyszukaj_pracownika("Anna Kowalczyk")
if pracownik:
    print(f"Znaleziony pracownik: {pracownik}")
else:
    print("Pracownik nie znaleziony")
# Filtrowanie pracowników według stanowiska
lista_managerow = system_kadrowy.pracownicy_po_stanowisku("Manager")
print("Lista Managerów:")
for manager in lista_managerow:
    print(manager)
# Obliczanie średniego wieku pracowników
sredni_wiek = system_kadrowy.sredni_wiek_pracownikow()
print(f"Średni wiek pracowników: {sredni_wiek}")
# Odczyt danych pracowników z pliku CSV
system_kadrowy.odczytaj_z_pliku_csv("pracownicy.csv")
# Wyświetlenie odczytanych danych pracowników
print("Odczytane dane pracowników:")
lista_pracownikow = system_kadrowy.lista_pracownikow()
for pracownik in lista_pracownikow:
    print(pracownik)