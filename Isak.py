Moral = 50 #Variabel som representerer lagmoralen gjennom historien, påvirkes av valgene med angitte negative/positive verdier
print("\n\n")
print(Moral)
print ("Silje VS Sivert\n"
"Silje og Sivert er uenige om design og teknologivalg. Det har eskalert til å bli en personkonflikt, og diskusjonene blir stadig mer emosjonelle. I tillegg begynner begge å trekke støtte fra sine nærmeste i gruppen, som fører til økt polarisering og dårligere fellesskap. Som prosjektleder har Erling et ansvar om å løse slike konflikter, og han står overfor to måter å løse konflikten på.\n" \

"\nValg A:\n Lufte konflikten i et plenum møte.\n" \
"" \
"\nValg B:\n Ha individuelle samataler med Silje og Sivert\n") \

Valg1 = input("Velg enten A eller B\n") #Siden disse resultatene er veldig nyanserte, har de mindre påvirkning på moralverdien.
if Valg1 == "A":
   Moral -= 5
   print ("\nÅpenheten fører til at konflikten blir synlig hos hele gruppen. Polariseringen i gruppen øker og teamet fortsetter med dårligere samhold, og risikoen for at uenigheten spres til andre arbeidsområder øker.")
elif Valg1 == "B":
    Moral += 5
    print ("\nSamtalene demper spenningen mellom Silje og Sivert, og Erling får bedre oversikt over konflikten. På den andre siden får gruppen lite innsyn, som fører til svekket åpenhet i gruppen.")
else: print ("\nErling klarer ikke ta et reelt valg, og ingeting skjer.")


print ("\n\n------------------------------------------------------------------------------------------------------------------------------------------\n\n")

print(Moral)
print ("Hamdi VS Jabir\n" \
"Konflikten mellom Hamdi og Jabir handler om hvordan innbyggere skal delta i digitalt medborgerskap, begge kommer med innspill, men likevel oppstår det en situasjon der partnerne kommer til en uenighet.\n" \
"\nValg A:\n" \
"Felles møte med Hamdi og Jabir.\n" \
"\nValg B:\n"
"Avvente problemet og håpet at konflikten løser seg selv.\n")

Valg2 = input("Velg enten A eller B\n")
if Valg2 == "A":
    Moral += 20
    print ("\nKonflikten håndteres tidlig, og begge partene får avklart forskjeller og misforståelser uten videre friksjon.")
elif Valg2 == "B":
    Moral -= 10
    print ("\nKonflikten fortsetter uten aktivt.")
else: print ("\nErling klarer ikke ta et reelt valg, og ingeting skjer.")


print ("\n\n------------------------------------------------------------------------------------------------------------------------------------------\n\n")

print(Moral)
print ("Lagmotivasjon\n" \
"Dette prosjektet består av et tverrfaglig team med bakgrunn fra forskjellige bransjer og fagfelt. \nHver deltaker har sine egne ekspertiser, prioriteringer og arbeidsmetoder, så i et slikt samarbeid vil det naturlig oppstå uenigheter og konflikter. \nAvhengig av hvor ofte og i hvilken grad dette skjer i gruppen, kan det ha en betydelig påvirkning på arbeidsmoralen, motivasjonen og effektiviteten i teamet som helhet. \nDerfor er det viktig at Erling som teamleder tar en vurdering om hvordan forholde seg til og eventuelt behandle samholdet i arbeidsgruppa\n" \
"\nValg A:\n" \
"Dedikere tid til teambuilding\n" \
"\nValg B:\n" \
"Prioritere fremdrift, med fokus på resultat\n")

Valg3 = input("Velg enten A eller B\n")
if Valg3 == "A":
    Moral += 20
    print("\nErling arrangerer sosiale arrangement og aktiviteter som styrker miljøet i teamet. \nDermed løftes arbeidsmoralen, motivasjonen og effektiviteten i prosjektarbeidet.")
elif Valg3 == "B" and Moral > 45:
    Moral += 0 #Om moralen er relativt god fra før, påvirker valg B ikke moralverdien.
    print("\nMotivasjonen i teamet fortsetter som den er uten påvirkning, og arbeidet fortsetter.")
elif Valg3 == "B" and Moral <= 45:
    Moral -= 15 #Når moralverdien er lav, påvirker valg B moralen negativt.
    print("\nUten et sosialt miljø i teamet blir den allerede dårlige stemningen enda værre. Motivasjonen og effektiviteten er meget lav.")
else: print("\nErling klarer ikke ta et reelt valg, og ingeting skjer.")


print ("\n\n------------------------------------------------------------------------------------------------------------------------------------------\n\n")

print(Moral)

if Moral > 85:
    print("Erling klarte å fikse alle konfliktene og fikk til å samle gruppen igjen slik at de kunne fortsette videre. \nDette gjør at medborgerportalen er på riktig tidslinje :D.")
elif Moral <= 85 and Moral > 40:
    print("Erling løser konfliktene delvis, men med noen kompromisser. \nRelasjonene mellom noen gruppemedlemmer fortsatt sårbare. \nMedborgerportalen er fortsatt på riktig kurs, men problemer kan fortsatt fort oppstå som kan føre til forsinkelser :/.")
else: print("Erling klarer ikke å løse konfliktene på en god måte, og mister samholdet i gruppen. \nEffektiviteten svekkes, og de må be om å forsinke medborgerportalen :(.")