# 4. Write a Python script to check whether a given key already exists in a dictionary. 

dict = {'Anna Kowalska': 111, 'Emilia Nowak': 112, 'Krystian Malinowski': 113}

def sprawdzanie (dict, key):
    if key in dict.keys ():
        print("Jest. Numer indeksu to: ", dict [key])
    else:
        print ("Nie ma")


key = 'Anna Kowalska'
sprawdzanie (dict, key)
  
key = 'Emilia Nowak'
sprawdzanie (dict, key)

