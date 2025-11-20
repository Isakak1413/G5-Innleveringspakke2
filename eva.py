poeng= 0 #veriabel for team medlemm 

print("Erling er prosjektleder for utviklingen av kommunens nye digitale medborgerportal.")
print("Teamet hans hadde en inspirerende start med mye energi, men sammarbeidet begynner å møte sine reelle prøver")
print("Hvordan skal Eriling hjelpe teamet løse konfliktene?")

print("første konflikten er mellom Silje og Sivert.")

print("ta et valg")
print ("1. Erling velger og snakke med de i plenum")
print ("2. Erling velger og snakke med de to hver for seg")

valg1 = input (" svar 1 eller 2:")
if valg1 == "1":
    poeng -= 1
    print("konflikten blir synlig for hele gruppen, polariseringen i gruppen øker og teamet fortsetter med dårlig samhold")

if valg1 == "2" :
    poeng += 1
    print("Skape trygghet for silje og sivert, som hjelper å løse konflikten")


print("Den andre konflikten er mellom Hamid og Jabir, de er uenige i hvordan innbyggerne skal kunne delta i digitale folkemøter.")

print("ta et valg")
print ("1. Erling velger å ta et møte mellom Hamdi og Jabir, samle dem til et kort møte.") 
print("2. Erling velger å avvente, å se om problemet løser seg")

valg2 = input ("svar 1 eller 2:")
if valg2 == "1":
    poeng += 1
    print("gir dem mulighet til å avklare misforståelser og få fram god kommunikasjon mellom partene.")
    
if valg2 == "2":
     poeng -= 1
     print("Kan bli mer personlig og vanskligre å løse senere. Frustrasjon kan bygge seg opp og påvikre arbeidsmiljøet negativt.")
        

print("Den tredje situasjonen er hvordan Erling kan bevare motivasjonen i teamet.")

print("ta et valg")
print ("1. Tid til relasjonsbygging")
print ("2. Prioritere fremdrift, med fokus på resultat")

valg3 = input  ("svar 1 eller 2:")
if valg3 == "1":
    poeng += 1
    print("styrker teamets arbeidsmoral og effektiviteten i arbeidet. Skape mer sosial trivsel og arbeidsmiljø")

elif valg3 == "2" and poeng > 0: 
    poeng -= 1
    print ("Erning hadde en samtale med gruppen, med siden de tidligre problemene ikke ble løst, blir dette negativt")


elif valg3 == "2" and poeng <= 0:
        poeng = 0
        print("Han tar det opp i plemun, men ingen reagerer")


if poeng >= 2:
     print(" Teamet løser konflikter/utfordringer og blir bedre.")
     
if poeng == 1:
        print("Teamet har ikke forandret seg mye.")

if poeng <= 0:
        print("Teamet fungerer dårlig og konfliktene/utfordringene blir verre.")
     

