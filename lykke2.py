# Interaktiv historie basert på storyline fra del 1 i oppgave 2 (IS-118)

print("Velkommen til prosjektspillet!")
print("Du er Erling, prosjektleder for utviklingen av kommunens digitale medborgerportal.")
print("Teamet ditt er i storming-fasen, og du må ta tre viktige valg.\n")

# ------------------ Beslutningspunkt 1 ------------------
print("BESLUTNING 1: Konflikten mellom Silje (UX-designer) og Sivert (IT-rådgiver).")
print("Den har gått fra sakskonflikt til personkonflikt.")

valg1 = input("Hva gjør du?\nA: Tar konflikten i plenum\nB: Tar individuelle samtaler med Silje og Sivert\n> ")

if valg1.lower() == "a":
    konsekvens1 = "plenum"
    print("\nDu tar det opp i plenum. Konflikten blir synlig for hele gruppen.")
    print("Åpenhet skaper innsikt, men polariseringen øker og stemningen forverres.\n")
elif valg1.lower() == "b":
    konsekvens1 = "individuelt"
    print("\nDu tar individuelle samtaler. Spenningen dempes og du får bedre oversikt.")
    print("Men gruppen får lite innsyn, og åpenheten svekkes.\n")
else:
    konsekvens1 = "ugyldig"
    print("\nUgyldig valg – vi antar du valgte individuelle samtaler.\n")

# ------------------ Beslutningspunkt 2 ------------------
print("BESLUTNING 2: Uenigheten mellom Hamdi og Jabir.")
print("Det ulmer mellom kulturavdelingen og brukerrepresentanten om folkemøteløsning.\n")

valg2 = input("Hva gjør du?\nA: Kaller inn til felles møte\nB: Avventer og håper det løser seg selv\n> ")

if valg2.lower() == "a":
    konsekvens2 = "møte"
    print("\nDu kaller inn til møte. De får avklart misforståelser, men føler seg litt korrigert.\n")
elif valg2.lower() == "b":
    konsekvens2 = "avvente"
    print("\nDu avventer. Konflikten eskalerer sakte og frustrasjonen øker i teamet.\n")
else:
    konsekvens2 = "ugyldig"
    print("\nUgyldig valg – vi antar du avventer.\n")

# ------------------ Beslutningspunkt 3 ------------------
print("BESLUTNING 3: Motivasjonen i teamet.")
print("Konfliktene har påvirket energi og arbeidsglede.\n")

valg3 = input("Hva gjør du?\nA: Sette av tid til relasjonsbygging og sosiale tiltak\nB: Prioritere fremdrift og fokusere på leveranser\n> ")

if valg3.lower() == "a":
    konsekvens3 = "relasjon"
    print("\nDu setter av tid til teambuilding. Forholdene styrkes, men tempoet blir litt lavere.\n")
elif valg3.lower() == "b":
    konsekvens3 = "fremdrift"
    print("\nDu fokuserer på fremdrift. Tidsplanen holder, men relasjonene er fortsatt sårbare.\n")
else:
    konsekvens3 = "ugyldig"
    print("\nUgyldig valg – vi antar du prioriterte fremdrift.\n")

# ------------------ Endepunkter ------------------
print("==== SLUTTRESULTAT ====")

# 1: Dårlig slutt – prosjektet forsinkes
if konsekvens1 == "plenum" and konsekvens2 == "avvente" and konsekvens3 == "fremdrift":
    print("Prosjektet mister samhold og må forsinkes. Konfliktene eskalerte og svekket samarbeidet.")
    print("Tidsplanen ryker og relasjonene er alvorlig svekket.")

# 2: Delvis løst – sårbare relasjoner
elif konsekvens3 == "fremdrift" or konsekvens2 == "avvente":
    print("Konfliktene er delvis løst, men relasjonene er fortsatt sårbare.")
    print("Prosjektet er på vei videre, men risikoen for nye konflikter er høy.")

# 3: Best mulig slutt – norming
else:
    print("Teamet gjenoppretter tillit og går inn i norming-fasen.")
    print("Konfliktene ble håndtert tidlig, motivasjonen steg, og prosjektet er på riktig spor!")

print("\nTakk for at du spilte prosjektspillet!")

