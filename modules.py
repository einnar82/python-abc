# import the whole module
# import datetime
# import time

# import specific class in module
from camelcase import CamelCase
from camelcase import CamelCase
from datetime import date
from time import time
from names import getName

c = CamelCase()
today = date.today()
timestamp = time()
print(today)
print(timestamp)
print(getName())
print(c.hump('hey'))
