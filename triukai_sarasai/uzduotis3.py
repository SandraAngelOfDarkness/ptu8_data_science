#Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
#Sukurti programą, kuri:
#Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
#Sudėtų ir atspausdintų visus sąrašo žodžius
#Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
#Patarimai:
#Naudoti filter arba comprehension, sum, " ".join()

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

#int_kiekis = sum(filter(lambda x: type(x) is int or type(x) is float, sarasas))
#print(int_kiekis)

#str_kiekis = filter(lambda x: type(x) is str, sarasas)
#print(" ".join(str_kiekis))

bool_kiekis = sum(x for x in sarasas if x == True)
print(bool_kiekis)