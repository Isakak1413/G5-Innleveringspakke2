# Min Digital Medborgerportal story

print("Velkommen til Erling sin historie om Digital Medborgerportal!")
print("Du skal ta tre valg som påvirker hvordan prosjektet går.\n")

# Variabler for å lagre poeng
tillit = 0 # noen svar gir mer tillit, variert fra type spørsmål
fremdrift = 0 # noen svar gir mer fremdrift, variet fra type spørsmål

# disse to er avhengig av hverandre, kun få minus tillit men plus fremdrift
# BESLUTNING 1 – SILJE OG SIVERT
print("Konflikt 1: Silje og Sivert krangler om design og teknologi.\n")

print("A: Ta konflikten åpent i plenum.")
print("B: Ta individuelle samtaler med begge to.\n")
valg1 = input("Hva velger du? (A/B): ")

 # Valg variabel vil brukes på alle situasjonene for å lagre en input

if valg1 == "A": 
    print("\nDu tar konflikten i plenum. Polariseringen øker og stemningen blir dårligere.\n")
    tillit -= 1
elif valg1 == "B":
    print("\nDu tar individuelle samtaler. Spenningen roer seg litt.\n")
    tillit += 1
else:
    print("\nUgyldig valg. Det tolkes som ingen handling – konflikten forverres.\n")
    tillit -= 1

# Disse svarene avhenger av inputen fra spilleren

# BESLUTNING 2 – HAMDI OG JABIR
print("Konflikt 2: Hamdi og Jabir er uenige om digitalt medborgerskap.\n")

print("A: Kalle dem inn til et felles møte.")
print("B: Avvente og håpe de løser det selv.\n")
valg2 = input("Hva velger du? (A/B): ")

if valg2 == "A":
    print("\nDu tar et møte med dem. Misforståelser ryddes opp.\n")
    tillit += 2
    fremdrift -= 1
elif valg2 == "B":
    print("\nDu venter. Konflikten vokser og skaper frustrasjon.\n")
    tillit -= 1
else:
    print("\nUgyldig valg. Ingenting skjer – konflikten vokser.\n")
    tillit -= 1

# BESLUTNING 3 – MOTIVASJON
print("Konflikt 3: Motivajonen i teamet synker.\n")

print("A: Arrangere teambuilding og sosial aktivitet.")
print("B: Prioritere fremdrift og fokus på resultater.\n")
valg3 = input("Hva velger du? (A/B): ").upper()

if valg3 == "A":
    print("\nTeamet får bedre samarbeid og stemning, men dere mister litt tid.\n")
    tillit += 2
    fremdrift -= 1
elif valg3 == "B":
    print("\nDere jobber raskt, men teamet blir stresset og mindre motivert.\n")
    tillit -= 1
    fremdrift += 2
else:
    print("\nUgyldig valg. Motivajonen faller videre.\n")
    tillit -= 1

# SLUTTRESULTAT
print(" SLUTTRESULTAT ")
print("Tillit-score:", tillit)
print("Fremdrift-score:", fremdrift)

# Bestemme endepunkt
if tillit >= 3 and fremdrift >= 0:
    print("ENDEPUNKT 3: Teamet gjenoppretter tillit og går videre til norming-fasen!")
elif tillit >= 0 and fremdrift >= -1:
    print("ENDEPUNKT 2: Konfliktene er delvis løst, men teamet er fortsatt sårbart.")
else:
    print("ENDEPUNKT 1: Prosjektet mister samhold og blir forsinket.")
# Endepunktet bestemmes av poeng av fremdrift og tillit
print("\nTakk for at du spilte Erling sin historie!")
