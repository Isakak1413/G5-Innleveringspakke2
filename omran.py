# erling_game_short.py
print("ERLING — beslutningsspill (kompakt)")
input("Trykk Enter for å starte...")

fremdrift = 0
sammenhold = 0

# Konflikt 1
print("\n1) Silje (UX) vs Sivert (IT) — design vs sikkerhet.")
print("A) Plenum    B) Individuelle samtaler")
valg1 = input("Velg A eller B: ").strip().lower()
if valg1 == "a":
    fremdrift -= 1; sammenhold += 2
else:
    sammenhold += 1

# Konflikt 2
print("\n2) Hamdi vs Jabir — digitalt medborgerskap, tidsnød.")
print("A) Kort møte    B) Avvente")
valg2 = input("Velg A eller B: ").strip().lower()
if valg2 == "a":
    fremdrift -= 1; sammenhold += 2
else:
    fremdrift += 1; sammenhold -= 2

# Motivasjon
print("\n3) Motivasjon — holde teamet oppe.")
print("A) Relasjonsbygging    B) Fokus på fremdrift")
valg3 = input("Velg A eller B: ").strip().lower()
if valg3 == "a":
    fremdrift -= 1; sammenhold += 3
else:
    fremdrift += 2; sammenhold -= 3

# Oppsummering
total = fremdrift + sammenhold
print("\n=== KONKLUSJON ===")
print(f"Fremdrift: {fremdrift} | Samhold: {sammenhold}")
print("-" * 30)

print("\nKonflikt 1:", "Plenum" if valg1 == "a" else "Individuelt")
print("Konflikt 2:", "Kort møte" if valg2 == "a" else "Avvente")
print("Motivasjon:", "Relasjon" if valg3 == "a" else "Fremdrift")

print("\nVurdering:")
if total >= 4:
    print("Sterkt resultat — god balanse mellom relasjoner og fremdrift.")
elif total >= 1:
    print("OK resultat — noen kompromisser.")
elif total >= -2:
    print("Risiko for konflikter, følg opp teamet.")
else:
    print("Problem: Konflikter uadressert — prosjektet kan lide.")
