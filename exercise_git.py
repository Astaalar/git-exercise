sklepy={
        "Warzywniak": ["ziemniaki", "brokół", "sałata"],
        "Piekarnia": ["chleb", "bułka", "rogal"]
}
for key, value in sklepy.items():
    str.upper(key)
    print("Lista zakupów")  
    print(f"Idę do {key.upper()}, i kupuję tam {value}")

    lista_zakupów=["ziemniaki", "brokół", "sałata", "chleb", "bułka", "rogal"]
for zakupy in lista_zakupów:
    print(f"W sumie kupuję {len(zakupy)} produktów.")
    break   
print("starts new lines")