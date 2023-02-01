# Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. 
# Parašykite generatorių, kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas. 
# Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau. 
# Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu, kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, 
# parašytų 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu. Sugalvokite, kaip apeiti šią problemą :).

pinas = '0001'
def atspeti_koda():
    skaicius = 0
    while skaicius < 10000:
        spejimas = f"{skaicius:0549}"
        if spejimas == pinas:
            print (f"{spejimas} atspetas skaicius")
            break
        yield spejimas
        skaicius += 1