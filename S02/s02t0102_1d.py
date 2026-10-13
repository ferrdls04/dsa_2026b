# Importando el modulo array de 
# la bibleoteca array y renombrado como arr
from array import array as arr

def print_array(input):
    print("[", end="")
    for element in input:
        print(element, end=",")
    print("\b]")

my_array = arr('i', [2,10,15,20])
print_array(my_array)

# Buscando el elmento 15
number_to_search = 100
counter = 0
for integer in my_array:

    if integer == number_to_search:
        print("🎉Numero encontrado")
        # Sirve para terminar el ciclo
        break
    #Incrementamos contador 
    counter += 1
    if counter == len(my_array):
        print("❌ Numero no encontrado")