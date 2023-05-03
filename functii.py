import math

"""
def suma_patratelor(a, b):
    c = a * a
    d = b * b
    return c + d
"""

def mutatie_animale(animal1, animal2):
    # verificam daca avem un sufix in animalul 1 care este continut in animalul 2 si concatenam cand l-am gasit
    # capra + rata = caprata, elefant + antilopa = elefantilopa
    # in caz ca primul termen este o lista de animale, atunci testam cu fiecare si aflam combinatiile
    # in caz ca al doilea termen este o lista de animale, le schimbam intre ele si facem mutatia
    # daca ambii termeni sunt liste, atunci afisam supraincarcare si returnam False
    if type(animal1) == type(5) or type(animal2) == type(5):
        print("Eroare: Mutatie imposibila cu numar")
        return False
    if type(animal1) == type(["a", "b"]) and type(animal2) == type(["a", "b"]):
        print("Eroare: Supraincarcare, prea multe animale de ambele parti")
        return False
    elif type(animal1) == type(["a", "b"]):
        lista_mutanti = []
        for x in animal1:
            lista_mutanti.append(mutatie_animale(x, animal2))
        return lista_mutanti
    elif type(animal2) == type(["a", "b"]):
        lista_mutanti = []
        for x in animal2:
            lista_mutanti.append(mutatie_animale(animal1, x))
        return lista_mutanti
    else:
        len1 = len(animal1)
        len2 = len(animal2)
        for i in range(0, len2):
            if animal1[len1 - 1 - i:] == animal2[:i + 1]:
                return animal1[:len1 - 1 - i] + animal2
        return animal1 + animal2
    # 2 functionala, 3 structurala, 1 distingerea unui mutant ramas in viata
    # coverage erase ; coverage run --branch foo.py ; coverage html -i

"""
Aici sunt testele din test_functii pentru a vedea daca se acopera toate ramurile
coverage erase ; coverage run --branch foo.py ; coverage html -i
se comenteaza aici testele daca vrem sa rulam mutantii
"""
mutatie_animale("elefant", "antilopa")
mutatie_animale("capra", "rata")
mutatie_animale(7, "pisica")
mutatie_animale("caine", 7)
mutatie_animale(["elefant", "capra", 6], ["rata"])
mutatie_animale(["elefant", "capra", 8], "rata")
mutatie_animale("papagal", ["albatros", "albina", 3])


"""
def media_geometrica_comparatie(a, b, c):
    #verificam daca, aproximand prin lipsa, media geometrica a doua numere este egala cu a treia
    produs = a * b
    medie = int(math.sqrt(produs))
    if medie == c:
        return True
    else:
        return False


def comparatie_fractii(a, b, c, d):
    fractie1 = a/b
    fractie2 = c/d
    if fractie1 > fractie2:
        return str(a) + "/" + str(b)
    elif fractie2 > fractie1:
        return str(c) + "/" + str(d)
    else:
        return "egale"


def numarare_vocale(cuvant):
    vocale = "aeiou"
    rezultat = 0
    for i in range(0, len(cuvant)):
        if cuvant[i] in vocale:
            rezultat += 1
    return rezultat


def interval_comun(a, b, c, d):
    # verificam daca exista un interval comun intre [a,b] si [c,d]
    if a <= c and b >= d:
        return "[" + str(c) + "," + str(d) + "]"
    elif a >= c and b <= d:
        return "[" + str(a) + "," + str(b) + "]"
    elif a <= c and b <= d and b >= c:
        return "[" + str(c) + "," + str(b) + "]"
    elif a >= c and b >= d and d >= a:
        return "[" + str(a) + "," + str(d) + "]"
    else:
        return "Nu avem interval comun"
"""
