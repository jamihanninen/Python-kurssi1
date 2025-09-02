Leiviskat=float(input("Anna leiviskät: "))
Naulat=float(input("Anna naulat: "))
Luodit=float(input("Anna luodit: "))

luodit_yhteensa=(Leiviskat*20*32+Naulat*32+Luodit)

grammat =(luodit_yhteensa*13.3)

kilogrammat = int(grammat // 1000)
jaannos_grammat = grammat % 1000


print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {jaannos_grammat:.2f} grammaa.")


