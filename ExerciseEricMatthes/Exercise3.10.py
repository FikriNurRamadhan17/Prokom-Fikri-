# Exercise 3.10
gunung = ['semeru', 'merapi', 'rinjani']
gunung.append('bromo')
gunung.insert(0, 'kerinci')
del gunung[1]
terakhir = gunung.pop()
gunung.remove('rinjani')
gunung.sort()
gunung.reverse()
print(sorted(gunung))
print(len(gunung))
print(gunung)

