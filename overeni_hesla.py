jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

if uzivatel.get(jmeno) == heslo:
    print(f"Ahoj {jmeno} vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
