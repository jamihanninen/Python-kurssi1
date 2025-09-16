
Pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamitta = 37
if Pituus < alamitta:
    puuttuu = alamitta - Pituus
    print(f"Kuha on alamittainen, laske se takaisin järveen. Pituudesta puuttuu {puuttuu:.1f}cm")

else:
    print("Kuha on sopivan mittainen!")