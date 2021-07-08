# 1. Write a Python script to sort (ascending and descending) a dictionary by value. 


import operator

słownik = {'Ala': 2, 'Ola': 4, 'Tola': 3, 'Lola': 1, 'Ela': 0}

print('Lista punktów: ', słownik)

posortowany_słownik = dict(sorted(słownik.items(), key=operator.itemgetter(1)))

print('Ranking: ', posortowany_słownik)
