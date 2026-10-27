from array import array as arr

# Parametro de mi cuadricula 
rows = 8
columns = 2 * rows - 1

# creando la grid 2D
matrix = []
# Construyendo el grid  
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la contruccion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))