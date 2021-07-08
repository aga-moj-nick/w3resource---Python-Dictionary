# 8. Write a Python script to merge two Python dictionaries.

def połączenie (słownik1, słownik2):
    return (słownik1.update (słownik2))

słownik1 = {1: 'a', 2: 'b', 3: 'c'}
słownik2 = {4: 'd', 5: 'e', 6: 'f'}

print (połączenie (słownik1, słownik2))
print (słownik1)

