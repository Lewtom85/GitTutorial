lista_zakupow = {
"piekarnia": ["chleb", "bulki", "paczki"],
"warzywniak": ["marchew", "seler", "rukola"]
}
#Wprowadzenie petli
for klucz, wartosc in lista_zakupow.items():
    print("Ide do sklepu:", (str(klucz).title()), "i kupuje:", (str(wartosc).title()))
#Dodatkowa zmienna do obliczne
suma = sum(len(v) for v in lista_zakupow.values())
print("W sumie kupuje", suma, "produktow.")
print("SPECJALNE POZDROWIENIA DLA RAFALA Z MADRYTU :)") 