shops={
        "Warzywniak": ["ziemniaki", "brokół", "sałata"],
        "Piekarnia": ["chleb", "bułka", "rogal"]
}
for key, value in shops.items():
    str.upper(key)
    print("Lista zakupów")  
    print(f"Idę do {key.upper()}, i kupuję tam {value}")

shopping_list=["ziemniaki", "brokół", "sałata", "chleb", "bułka", "rogal"]
for shopping in shopping_list:
    print(f"W sumie kupuję {len(shopping)} produktów.")
    