# 14. Write a Python program to sort a given dictionary by key. 


słownik = {'Ala': 15,
           'Ola': 20,
           'Ela': 25}

for key in sorted (słownik):
    print (key, słownik [key])



słownik1 = {'Kowalska Anna': 100,
            'Słowacka Krystyna': 98,
            'Dąbrowski Mateusz': 50,
            'Adamski Zygmunt': 75,
            'Zuziak Julia': 48,
            'Tomczak Martyna': 99,
            'Jaworski Adam': 15}

for key in sorted (słownik1):
    print (key, słownik1 [key])


słownik2 = {'Kowalska Anna': 100,
            'Słowacka Krystyna': 98,
            'Dąbrowski Mateusz': 50,
            'Adamski Zygmunt': 75,
            'Zuziak Julia': 48,
            'Tomczak Martyna': 99,
            'Jaworski Adam': 15}

for value in sorted (słownik2):
    print (value, słownik2 [value])
