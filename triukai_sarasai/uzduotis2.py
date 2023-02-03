<<<<<<< HEAD
#Sukurti programą, kuri:
#Sukurtų sąrašą iš skaičių nuo 0 iki 50
#Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
#Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
#Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų. Šį sąrašą (list masyvą) priskirti naujam kintamajam.
#Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
#Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
#Patarimai:
#Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
from statistics import mean, median

sarasas = list(range(51))
#padauginti = [x*10 for x in sarasas]
#print(padauginti)

#dalinasi = [x for x in sarasas if x % 7 == 0]
#print(dalinasi)

kvadratu = [x**2 for x in sarasas]
#print(kvadratu)

#print(sum(kvadratu))
#print(min(kvadratu))
#print(max(kvadratu))
#print(mean(kvadratu))
#print(median(kvadratu))

kvadratu.sort(reverse=True)
print(kvadratu)
=======
#Sukurti programą, kuri:
#Sukurtų sąrašą iš skaičių nuo 0 iki 50
#Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
#Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
#Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų. Šį sąrašą (list masyvą) priskirti naujam kintamajam.
#Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
#Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
#Patarimai:
#Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
from statistics import mean, median

sarasas = list(range(51))
#padauginti = [x*10 for x in sarasas]
#print(padauginti)

#dalinasi = [x for x in sarasas if x % 7 == 0]
#print(dalinasi)

kvadratu = [x**2 for x in sarasas]
#print(kvadratu)

#print(sum(kvadratu))
#print(min(kvadratu))
#print(max(kvadratu))
#print(mean(kvadratu))
#print(median(kvadratu))

kvadratu.sort(reverse=True)
print(kvadratu)
>>>>>>> 65fbaf748aab15afb7c2ef833ec209f0f4e61b66
