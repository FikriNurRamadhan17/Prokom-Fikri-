# Exercise 4.11
pizzas = ['pepperoni', 'hawaiian', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('veggie')
friend_pizzas.append('meat')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

