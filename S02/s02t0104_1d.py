# Importando funcion array
# del modulo array 
# como arr
from array import array as arr

# Importado una funcion de otra 
# Archivo
from s02t0102_1d import print_array

my_array = arr('i', [2,10,15,20,10])

print("---ANTES DE LA ELIMINACIÓN---")
print_array(my_array)

# Eliminación
try:
   my_array.remove(100)
except:
    print(f"⚠ no se encuentra en el arreglo")
print("---DESPUES DE LA ELIMINACIÓN---")
print_array(my_array)