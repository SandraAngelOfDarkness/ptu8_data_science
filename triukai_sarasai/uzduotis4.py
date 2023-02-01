#Sukurti programą, kuri:
#Turėtų klasę Zmogus, su savybėmis vardas ir amzius
#Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
#Inicijuoti kelis Zmogus objektus su vardais ir amžiais
#Įdėti sukurtus Zmogus objektus į naują sąrašą
#Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
#Patarimai:
#Naudoti sorted, attrgetter, reverse, funkciją repr

from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

d1 = Zmogus("Jonas", 39)
d2 = Zmogus("Antanas", 25)
d3 = Zmogus("Maryte", 69)
sarasas = [d1, d2, d3]

#surusiuotas = sorted(sarasas, key=lambda e: e.vardas)
#print(surusiuotas)

#surusiuotas = sorted(sarasas, key=lambda e: e.vardas, reverse=True)
#print(surusiuotas)

#surusiuotas = sorted(sarasas, key=lambda e: e.amzius)
#print(surusiuotas)

surusiuotas = sorted(sarasas, key=lambda e: e.amzius, reverse=True)
print(surusiuotas)

