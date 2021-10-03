from PyCovid import *

world=get_stat('world')
print(world)
print(world['cases'])

uzbekistan=get_stat('uzbekistan')
print(uzbekistan)
print(uzbekistan['cases'])

print(get_flag('world'))
print(get_flag('uzbekistan'))