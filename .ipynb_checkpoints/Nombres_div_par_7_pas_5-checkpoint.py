'''Create a Python program that identifies all numbers between 100 and 300 (inclusive) that are divisible by 7 but not multiples of 5. 
The identified numbers should be displayed in a single line, separated by commas.'''

import math

liste_soluces = []

def test_7(nombre):
    if nombre%7 == 0:
        return True
    else:
        return False
    
def test_5(nombre):
    if nombre%5 == 0:
        return True
    else:
        return False

def find_numbers(mini, maxi):
    test_divis = mini
    while test_divis <= maxi:
        if test_7(test_divis) and not test_5(test_divis):
        # if test_7(test_divis) == True & test_5(test_divis) == False:
            liste_soluces.append(test_divis)
        test_divis += 1

find_numbers(100,300)
print(liste_soluces)

