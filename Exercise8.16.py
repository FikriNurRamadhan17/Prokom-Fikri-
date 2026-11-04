# Exercise 8.16
# Cara 1: import seluruh modul
import city_module
city_module.describe_city('surakarta')

# Cara 2: import fungsi tertentu
from city_module import describe_city
describe_city('jakarta')

# Cara 3: import fungsi dengan alias
from city_module import describe_city as dc
dc('tokyo', 'japan')

# Cara 4: import modul dengan alias
import city_module as cm
cm.describe_city('paris', 'france')

# Cara 5: import semua fungsi
from city_module import *
describe_city('bandung')
