lista_zakupow = {
"piekarnia": ["chleb", "bulki", "paczki"],
"warzywniak": ["marchew", "seler", "rukola"]
}
for klucz, wartosc in lista_zakupow.items():
    print("Ide do sklepu:", (str(klucz).title()), "i kupuje:", (str(wartosc).title()))
suma = sum(len(v) for v in lista_zakupow.values())
print("W sumie kupuje", suma, "produktow.") 