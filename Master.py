
print("\n\n-----------------------------------START-----------------------------------\n")
print("\nErling har oppdaget at noen konflikter i gruppen har kommet opp under storming-fasen.\nHan har 3 konflikter som må håndteres for å forbedre gruppedynamikken.")

Moral = 50 # Global variabel for å følge moralen i gruppen når man velger valg. Denne verdien vil gå opp og ned avhenngig av valgene. Begynner på 50 for å så kunne gå opp å ned med mer og fortsatt være oversiktelig.


print("\n\n-----------------------------------KONFLIKT 1-----------------------------------\n")
print ("Moralscore:",(Moral),"\n")
print("Silje og Sivert er uenige om design og teknologivalg. Det har eskalert til å bli en personkonflikt, og diskusjonene blir stadig mer emosjonelle. \nI tillegg begynner begge å trekke støtte fra sine nærmeste i gruppen, som fører til økt polarisering og dårligere fellesskap.\n")
print("Skal Erlen:\n" \
" 1. Ta konflikten opp i plenum.\n" \
" 2. Snakk med Silje og Sivert induvielt.\n")

valg1 = input("Skriv inn 1 eller 2 for å velge: \n") # Vi bruker variabel for å samle inputen for å bruke den senere for å bestemme konsekvens. Vi gjør dette på alle tre situasjonene som oppsto.

if valg1 == "1":
    Moral += 5
    print("\nErling arrangerer et gruppemøte. Under møtet blir konflikten mer intens, og Silje og Sivert føler seg enda mer misforstått.")
    print("Dette fører til økt spenning i gruppen, og Erling må finne en annen måte å håndtere situasjonen på.")
# if seteninger for å ha to mulige konsekvenser som skjer avhengig av svar. Dette gjør vi på alle tre situasjonene.
elif valg1 == "2":
    Moral -= 5
    print("\nSamtalene demper spenningen mellom Silje og Sivert, og Erling får bedre oversikt over konflikten.")
    print("På den andre siden får gruppen lite innsyn, som fører til svekket åpenhet i gruppen.")

else:
    print("\nErling tar ikke et valg og ender opp med å synke moralen i gruppa enda mer, Erling burde forsøke å håndtere fremtidige konflikter")    
    Moral -= 10

print("\n\n-----------------------------------KONFLIKT 2-----------------------------------\n")
print ("Moralscore:",(Moral),"\n")
print("Neste situasjon involverer Hambi og Jabir det er spenning mellom dem på grunn av uenighet om hvordan innbyggerne skal kunne delta i digitale folkemøter.\n")
print("Skal Erlen:\n" \
" 1. Fasilitere et møte der Hambi og Jabir kan dele sine synspunkter og finne felles grunnlag.\n" \
" 2. Velge ikke å ta en prat og bare lar det ligge.\n")

valg2 = input("Skriv inn 1 eller 2 for å velge: \n")
if valg2 == "1":
    Moral += 20
    print("\nErling fasiliterte et møte. Hambi og Jabir får muligheten til å uttrykke sine synspunkter, og de oppdager at de har mer til felles enn de trodde. Det at Erling tar det opp tidlig hjelper dem å finne en løsning.")
    print("\nDette fører til bedre forståelse og samarbeid mellom dem.")
elif valg2 == "2":
    Moral -= 10
    print("\nSiden Erling valgte å ikke ta opp konflikten, eskalerte spenningen mellom Hambi og Jabir. De unngår hverandre og samarbeidet deres lider som et resultat.")
    print("Konflikten mellom dem vedvarer, og Erling må finne en annen måte å fremme samarbeid på.")
else: 
    Moral -= 10
    print("\nErling tar ikke et valg og ender opp med å synke moralen i gruppa enda mer, Erling burde forsøke å håndtere fremtidige konflikter")    


print("\n\n-----------------------------------KONFLIKT 3-----------------------------------\n")
print ("Moralscore:",(Moral),"\n")
print("Den siste situasjonen involverer Erling og hvordan han selv kan motivere gruppen etter de tidligere konfliktene.\nHvordan Erling har tidligere valgt å håndtere konfliktene har påvirket moralen i gruppen\n")
print("Skal Erlen:\n" \
" 1. Organisere en teambuilding-aktivitet for å styrke gruppens samhold.\n" \
" 2. Prioritere fremdiften i prosjektet og å fokus på resultatet.\n")
      
valg3 = input("Skriv inn 1 eller 2 for å velge: \n")
if valg3 == "1":
    Moral += 20
    print("\nErling organiserer en teambuilding-aktivitet. Gjennom samarbeidsøvelser og sosiale aktiviteter, styrkes gruppens samhold betydelig.")
    print("\nGruppen føler seg mer motivert og engasjert i arbeidet sitt.")

elif valg3 == "2" and Moral <=45:
    Moral -= 15
    print("\nValget om å fokusere på fremdrift uten å adressere de underliggende konfliktene fører til at gruppens moral synker ytterligere.")
    print("\nMotivasjonen i gruppen forblir lav, og Erling må finne andre måter å inspirere dem på.")
elif valg3 == "2":
    Moral += 0
    print("\nErling sitt valg endrer ikke på moralen i gruppen på en nevneverdig måte")
    print("\nGruppen blir verken mer eller mindre motivert av dette valget.")
else:
    print("\nErling tar ikke et valg og ender opp med å synke moralen i gruppa enda mer, Erling burde forsøke å håndtere fremtidige konflikter")    
    Moral -= 10

print("\n\n-----------------------------------KONKLUSJON-----------------------------------\n")
# Til slutt er det moral du har fått av de forskjellige sprøsmålene som velger hvilket endepunkt du får
print ("Moralscore: ",(Moral))
if Moral > 85:
    print("\nGruppe dynamikken har forbedret seg betydelig takket være Erlings valg. Gruppen jobber nå mer effektivt sammen og er motivert for fremtidige utfordringer.")
elif Moral < 40:
    print("\nGruppe dynamikken har forverret seg på grunn av Erlings valg. Konfliktene vedvarer, og gruppen sliter med å samarbeide effektivt.")
else:
    print("\nGruppe dynamikken har sett bedre tider men også verre. Det er derfor rom for forbedring i gruppe damymikken.")

print("\nTakk for at du hjalp Erling med å navigere gjennom disse utfordringene i gruppen!")

input("\nTrykk Enter for å avslutte spillet...") # bare for å gjøre det enklere å skjønne når man er ferdig med spillet
