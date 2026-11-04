# Exercise 7.10
responses = {}
polling_active = True

while polling_active:
    name = input("\nSiapa namamu? ")
    place = input("Kalau bisa mengunjungi satu tempat di dunia, ke mana kamu pergi? ")
    responses[name] = place

    repeat = input("Ada orang lain yang mau menjawab? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Hasil Polling ---")
for name, place in responses.items():
    print(f"{name} ingin pergi ke {place}.")
    
    