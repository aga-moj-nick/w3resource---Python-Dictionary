# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys


def słownik ():
    nowy_słownik = {i: i ** 2 for i in range (1, 16)}
    print (nowy_słownik)
słownik ()
