# Exercise 7.4
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"Oke, {topping} akan ditambahkan ke pizzamu.")