Moral = 50 # Global variabel for å følge moralen i gruppen når man velger valg. Denne verdien vil gå opp og ned avhenngig av valgene.

print("\n Erling har oppdaget at noen konflikter i gruppen har kommet opp under storming-fasen. Erling har 3 situasjoner han må håndtere for å forbedre gruppedynamikken. Den første av de er mollom gruppemedlemmer Silje og Sivert.")
print("\n Han vurderer to alternativer for å håndtere situasjonen:")


print("-----------Konflikt 1-----------")

print(" Ta et valg : " \
" 1. Ta konflikten opp i plenum." \
" 2. Snakk med Silje og Sivert induvielt.")

valg1 = input("Skriv inn 1 eller 2 for å velge: ") # Jeg bruker variabel for å samle inputen for å bruke den senere for å bestemme konsekvens

if valg1 == "1":
    Moral += 5
    print("Erling arrangerer et gruppemøte. Under møtet blir konflikten mer intens, og Silje og Sivert føler seg enda mer misforstått.")
    print("Dette fører til økt spenning i gruppen, og Erling må finne en annen måte å håndtere situasjonen på.")
# if seteninger for å ha to mulige konsekvenser som skjer avhengig av svar. Dette gjør jeg på alle tre situasjonene.
elif valg1 == "2":
    Moral -= 5
    print("Erling arrangerer et gruppemøte. Under møtet blir konflikten mer intens, og Silje og Sivert føler seg enda mer misforstått.")
    print("Dette fører til økt spenning i gruppen, og Erling må finne en annen måte å håndtere situasjonen på.")
    

print("-----------Konflikt 2-----------")

print("Neste situasjon involverer Hambi og Jabir det er spenning mellom dem på grunn av uenighet om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print("Erling vurderer to løsninger for å løse konflikten:")


print(" Ta et valg : " \
" 1. Fasilitere et møte der Hambi og Jabir kan dele sine synspunkter og finne felles grunnlag." \
" 2. Erling velger ikke å ta en prat og bare lar det ligge.")

valg2 = input("Skriv inn 1 eller 2 for å velge: ")
if valg2 == "1":
    Moral += 20
    print("\n Erling fasiliterte et måte. Hambi og Jabir får muligheten til å uttrykke sine synspunkter, og de oppdager at de har mer til felles enn de trodde. Det at Erling tar det opp tidlig hjelper dem å finne en løsning.")
    print("\n Dette fører til bedre forståelse og samarbeid mellom dem.")

elif valg2 == "2":
    Moral -= 10
    print("\n Siden Erling valgte å ikke ta opp konflikten, eskalerte spenningen mellom Hambi og Jabir. De unngår hverandre og samarbeidet deres lider som et resultat.")
    print("Konflikten mellom dem vedvarer, og Erling må finne en annen måte å fremme samarbeid på.")

print("-----------Konflikt 3----------")


print("\n Den siste situasjonen involverer Erling og hvordan han selv kan motivere gruppen etter de tidligere konfliktene. Hvordan Erling har tidligere valgt å håndtere konfliktene har påvirket moralen i gruppen.")
print("\n To løsninger vurderes av Erling for å motivere teamet:")

print("\n Ta et valg : " \
      " 1. Organisere en teambuilding-aktivitet for å styrke gruppens samhold." \
      " 2. Prioritere fremdiften i prosjektet og å fokus på resultatet. ")
valg3 = input("Skriv inn 1 eller 2 for å velge: ")
if valg3 == "1" and Moral > 45:
    Moral += 20
    print("\n Erling organiserer en teambuilding-aktivitet. Gjennom samarbeidsøvelser og sosiale aktiviteter, styrkes gruppens samhold betydelig.")
    print("\n Gruppen føler seg mer motivert og engasjert i arbeidet sitt.")

elif valg3 == "2" and Moral <=45:
    Moral -= 15
    print("\n Valget om å fokusere på fremdrift uten å adressere de underliggende konfliktene fører til at gruppens moral synker ytterligere.")
    print("\n Motivasjonen i gruppen forblir lav, og Erling må finne andre måter å inspirere dem på.")
else :
    Moral += 0
    print("Erling sitt valg endrer ikke på moralen i gruppen på en nevneverdig måte")
    print("Gruppen blir verken mer eller mindre motivert av dette valget.")

# Til slutt er det moral du har fått av de forskjellige sprøsmålene som velger hvilket endepunkt du får
if Moral > 85:
    print("\n Gruppe dynamikken har forbedret seg betydelig takket være Erlings valg. Gruppen jobber nå mer effektivt sammen og er motivert for fremtidige utfordringer.")
elif Moral < 40:
    print("\n Gruppe dynamikken har forverret seg på grunn av Erlings valg. Konfliktene vedvarer, og gruppen sliter med å samarbeide effektivt.")
else :
    print("\n Gruppe dynamikken har sett bedre tider men også verre. Det er derfor rom for forbedring i gruppe damymikken.")

print("\n Takk for at du hjalp Erling med å navigere gjennom disse utfordringene i gruppen!")

input("\nTrykk Enter for å avslutte spillet...")
