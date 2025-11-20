input("nTrykk Enter for å fortsette ")

def pause():
    input("\nTrykk Enter for å fortsette...")

def beslutning(prompt, a_text, b_text):
    print("\n" + prompt)
    print("A) " + a_text)
    print("B) " + b_text)
    choice = input("Velg A eller B: ").strip().lower()
    if choice not in ("a", "b"):
        print("Ugyldig valg — jeg tolker som B.")
        return "b"
    return choice

def outcome_conflict1(choice):
    if choice == "a":
        print("\nDu valgte p" \
        "lenum. Åpen diskusjon fører til mer innsikt og felles eierskap, men litt distraksjon fra arbeidet.")
        return {"fremdrift": -1, "sammenhold": +2}
    else:
        print("\nDu valgte individuelle samtaler. Partene føler seg hørt, mindre spenning i plenum, men mindre felles eierskap.")
        return {"fremdrift": +0, "sammenhold": +1}

def outcome_conflict2(choice):
    if choice == "a":
        print("\nDu kaller Hamdi og Jabir inn til et kort møte. Konflikten avklares tidlig og løsninger integreres — risiko for eskalering reduseres.")
        return {"fremdrift": -1, "sammenhold": +2}
    else:
        print("\nDu avventer (unnvikende). På kort sikt går prosjektet videre, men risikoen for at frustrasjon vokser og senere sinker arbeidet øker.")
        return {"fremdrift": +1, "sammenhold": -2}

def outcome_motivation(choice):
    if choice == "a":
        print("\nDu prioriterer relasjonsbygging. Teamet får økt tillit og motivasjon; langsiktig produktivitet øker.")
        return {"fremdrift": -1, "sammenhold": +3}
    else:
        print("\nDu fokuserer på fremdrift uten relasjonsarbeid. Kort sikt: mulig raskere leveranser, men høyere turnover og lavere motivasjon.")
        return {"fremdrift": +2, "sammenhold": -3}

def summarize(score):
    print("\n=== Sammendrag av utfallet ===")
    total = score["fremdrift"] + score["sammenhold"]
    print(f"Poeng — Fremdrift: {score['fremdrift']}, Samhold: {score['sammenhold']}")
    if total >= 3:
        print("Resultat: Sterkt team og god fremdrift. Valgene støttet både samarbeid og produktivitet.")
    elif total >= 0:
        print("Resultat: Moderat balanse. Noe avveining mellom fremdrift og relasjoner.")
    else:
        print("Resultat: Problem. Relasjonen i teamet svekkes og prosjektfremdriften kan lide i neste fase.")
    print("Tips: Tidlig håndtering av konflikter + relasjonsbygging gir ofte best langsiktige resultater.")

def main():
    print("=== Erling: beslutninger som prosjektleder ===")
    print("Bakgrunn: Teamet er i stormingfase. Du er prosjektleder Erling og skal ta tre valg.")
    pause()

    score = {"fremdrift": 0, "sammenhold": 0}

    # Konflikt 1: Silje og Sivert
    c1 = beslutning(
        "Konflikt 1 — Silje (UX) vs Sivert (IT). Hvordan løser du konflikten?",
        "Lufte konflikten i plenum (åpen diskusjon).",
        "Individuelle samtaler med hver av partene."
    )
    res1 = outcome_conflict1(c1)
    score["fremdrift"] += res1["fremdrift"]
    score["sammenhold"] += res1["sammenhold"]
    pause()

    # Konflikt 2: Hamdi og Jabir
    c2 = beslutning(
        "Konflikt 2 — Hamdi vs Jabir om digitalt medborgerskap. Hvordan handler du?",
        "Kalle inn begge til et kort møte for å avklare (aktiv, forebyggende).",
        "Avvente / ikke gripe inn (unnvikende)."
    )
    res2 = outcome_conflict2(c2)
    score["fremdrift"] += res2["fremdrift"]
    score["sammenhold"] += res2["sammenhold"]
    pause()

    # Motivasjon
    c3 = beslutning(
        "Motivasjon — Hvordan vil du bevare teamets motivasjon?",
        "Dedikere tid til relasjonsbygging og teamaktiviteter.",
        "Prioritere kortsiktig fremdrift og la relasjoner være sekundært."
    )
    res3 = outcome_motivation(c3)
    score["fremdrift"] += res3["fremdrift"]
    score["sammenhold"] += res3["sammenhold"]
    pause()

    summarize(score)

if __name__ == "__main__":
    main()
