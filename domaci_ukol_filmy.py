sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

#sjednocení filmů do jednoho slovníku, kde jednotlivé filmy jsou puvodni slovniky
filmy = {film_1["jmeno"]: film_1, film_2["jmeno"]: film_2, film_3["jmeno"]: film_3}

#uvodni vypis pro uzivatele
print("Vítej v našem filmovém slovníku!".upper().center(62))
print(oddelovac)
# tady bych normalne joinul sluzby, ale vystup ma byt misto 3. sluzby("seznam reziseru") - "doporuc film"
seznam_sluzeb = " | ".join((sluzby[0],sluzby[1], "doporuč film")) 
print(seznam_sluzeb.center(62))
print(oddelovac)
print()


#Zobrazi dostupne filmy
print(str(sluzby[0].capitalize() + ":").center(62))
print(oddelovac)
print(*filmy.keys(), sep = ", ")        # * tzv rozbalí klíče do jednotlivých argumentů 
print(oddelovac)
print()

#Zobrazi detaily o filmu
print(sluzby[1].capitalize() + ":")
print(oddelovac)
print(filmy["The Dark Knight"])
print(oddelovac)
print()

#Zobrazi seznam reziseru
print("Všichni režiséři:")
print(oddelovac)
# tady to mi asi prijde, ze chteli, abychom udelali... jinak vubec nechapu... to zadani je fakt na pytel
reziseri = set()
for film in filmy.keys():
    reziseri.add(filmy[film]["reziser"])
    
print(reziseri)
print(oddelovac)
print()
    