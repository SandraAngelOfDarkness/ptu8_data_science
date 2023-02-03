<<<<<<< HEAD
#Sukurti programą, kuri:
#Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
#Patarimai:
#Naudoti map (su lambda) arba comprehension, " ".join()

sakinys = "The Zen of Python"

#naujas = map(lambda x: x + "!", sakinys.split())
#print(" ".join(naujas))

naujas = [x + "!" for x in sakinys.split()]
=======
#Sukurti programą, kuri:
#Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
#Patarimai:
#Naudoti map (su lambda) arba comprehension, " ".join()

sakinys = "The Zen of Python"

#naujas = map(lambda x: x + "!", sakinys.split())
#print(" ".join(naujas))

naujas = [x + "!" for x in sakinys.split()]
>>>>>>> 65fbaf748aab15afb7c2ef833ec209f0f4e61b66
print(" ". join(naujas))