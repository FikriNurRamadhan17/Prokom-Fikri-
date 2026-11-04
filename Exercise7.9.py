# Exercise 7.9
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ayam', 'telur', 'pastrami']
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)
    
    