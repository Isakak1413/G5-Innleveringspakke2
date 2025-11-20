#1. Introduksjon
print("\033[1m\033[33mVelkommen til prosjektspillet\033[0m\033[0m")
print("Du er spilleren Erling, prosjektleder for kommunens medborgersentral.")
print("Du skal ta tre beslutninger som påvirker konflikter")
score = 0
#2. Beslutning 1 - Silje og Sivert
print("\033[1m\033[34mBeslutning 1: Konflikten mellom Silje og Sivert.\033[0m\033[0m")
print("Mellom Silje og Sivert har det oppstått uenigheter om design og teknologivalg. Disse uenighetene har eskalert til å bli en personkonflikt, og diskusjonene blir stadig mer emosjonelle. I tillegg begynner begge å trekke støtte fra sine nærmeste i gruppen, som fører til økt polarisering og dårligere fellesskap. Som prosjektleder har Erling et ansvar om å løse slike konflikter, og han står overfor to måter å løse konflikten på.")
print("\033[34mA: Ta opp konflikten i plenum.\036")
print("\033[34mB: Ha individuelle samtaler med dem.\036")

valg1 = input("\033[37mVelg A eller B: ").upper()

if valg1 == "A":
    print("\n\033[1m\033[31mDu valgte å ta opp konflikten i plenum.\033[0m\033[0m")
    print("Åpenheten fører til at konflikten blir synlig hos hele gruppen. Polariseringen i gruppen øker og teamet fortsetter med dårligere samhold, og risikoen for at uenigheten spres til andre arbeidsområder øker.\n")
    # score += 0
elif valg1 == "B":
    print("\n\033[1m\033[32mDu valgte individuelle samtaler med Silje og Sivert.\033[0m\033[0m")
    print("Samtalene demper spenningen mellom Silje og Sivert, og Erling får bedre oversikt over konflikten. På den andre siden får gruppen lite innsyn, som fører til svekket åpenhet i gruppen.\n")
    score += 1
else:
    print("\nUgyldig valg, du burde valgt A eller B. Vi antar B videre.\n")
    score += 1
#3. Beslutning 2 - Hamdi og Jabir
print("\033[1m\033[35mBeslutning 2: Uenighet mellom Hamdi og Jabir.\033[0m\033[0m")
print("Konflikten mellom Hamdi og Jabir handler om hvordan innbyggere skal delta i digitalt medborgerskap, begge kommer med innspill, men likevel oppstår det en situasjon der partnerne kommer til en uenighet. Erling er prosjektleder og har to alternativer på hvordan han kan komme fram til en problemløsning.")
print("\033[35mA: Kalle inn til felles møte for å avklare uenigheten.\033[0m")
print("\033[35mB: Avvente og håpe at de finner ut av det selv\033[0m")

valg2 = input("Velg A eller B: ").upper()

if valg2 == "A":
    print("\n\033[1m\033[32mDu valgte felles møte.\033[0m\033[0m")
    print("Når Erling merker uenigheten kaller han dem inn til et møte, han bruker strategi som er i tråd med problemløsning og integrasjon. Det som skjer i møtet er at begge forklarer hva de mener og hvorfor, de analyserer konflikten ved integrerende tilnærming.\n")
    score += 1
elif valg2 == "B":
    print("\n\033[1m\033[31mDu valgte å avvente.\033[0m\033[0m")
    print("Dersom Erling og han antar konflikten er for liten til å bruke tid på, er det et typisk trekk ved unnvikende konflikt. Effektiviteten kommer til å synke fordi konflikter kommer til å bli håndtert tilfeldig, misforståelser begynner å vokse. Erling må da bruke mer tid og energi på konflikten enn om han hadde tatt tak i problemet tidligere.\n")
    score += 0
else:
    print("\nUgyldig valg, du burde valgt A eller B. Vi antar B videre.\n")
    score += 0
#4. Beslutning 3 - Motivasjon
print("\033[1m\033[36mBeslutning 3: Motivasjon i teamet.\033[0m\033[0m")
print("Dette prosjektet består av et tverrfaglig team med bakgrunn fra forskjellige bransjer og fagfelt. Hver deltaker har sine egne ekspertiser, prioriteringer og arbeidsmetoder, så i et slikt samarbeid vil det naturlig oppstå uenigheter og konflikter. Avhengig av hvor ofte og i hvilken grad dette skjer i gruppen, kan det ha en betydelig påvirkning på arbeidsmoralen, motivasjonen og effektiviteten i teamet som helhet. Derfor er det viktig at Erling som teamleder tar en vurdering om hvordan forholde seg til og eventuelt behandle samholdet i arbeidsgruppa.")
print("\033[36mA: Sette av tid til relasjonsbygging og sosiale tiltak.\033[0m")
print("\033[36mB: Prioritere kun fremdrift og leveranser.\033[0m")

valg3 = input("Velg A eller B: ").upper()

if valg3 == "A":
    print("\033[1m\n\033[32mDu valgte relasjonsbygging.\033[0m\033[0m")
    print("Teamet deltar i en workshop eller sosial sammenkomst. De får kommunisert bedre sammen, konflikter reduseres og motivasjonen øker. Samarbeidet blir mer trygt og effektivt. På samme tid mister teamet tid til prosjektarbeidet, og fristen for ferdigstilling av prototypen blir mer krevende.\n")
    score += 1
elif valg3 == "B":
    print("\033[1m\n\033[31mDu valgte å fokusere på leveranser.\033[0m\033[0m")
    print("Teamet jobber intensivt og får rask progresjon. På kort sikt oppleves dette effektivt, men flere føler seg oversett og stresset. Uenigheter forblir uløst og motivasjonen i teamet synker betraktelig. Teamet står derfor i en situasjon der nye konflikter kan oppstå senere i prosjektet.\n")
    score += 0
else:
    print("\nUgyldig valg, du burde valgt A eller B. Vi antar B videre.\n")
    score += 0

print("\033[1m\033[33m-------------------------------------Slutt på historien-------------------------------------\033[0m\033[0m")


if score == 3:
    print("\033[1m\033[32mSluttutfall 1:\033[0m\033[0m")
    print("Erling håndterer alle konfliktene på en konstruktiv måte. Teamet gjenoppretter tilliten, samarbeidet stabiliseres, og prosjektet går videre som planlagt.")
elif score == 1 or score == 2:
    print("\033[1m\033[90mSluttutfall 2:\033[0m\033[0m")
    print("Konfliktene håndteres delvis, og teamet oppnår et minimum av samarbeid. Relasjonene er fortsatt sårbare, og prosjektet holder fremdriften, men med risiko for nye hindringer.")
else:
    print("\033[1m\033[31mSluttutfall 3:\033[0m\033[0m")
    print("Konfliktene forblir uløste, polariseringen øker og samholdet svekkes. Teamet klarer ikke å komme videre, og prosjektet må utsettes.")
    
input("\nTrykk Enter for å avslutte spillet...")