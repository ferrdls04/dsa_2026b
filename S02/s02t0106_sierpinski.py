from array import array as arr

# Parametro de mi cuadricula 
rows = 10
columns = 2 * rows - 1

# Funcion para imprimir matrix
def print_matrix(matrix):
    for row in matrix:
        print(list(row))

# creando la grid 2D
matrix = []
# Construyendo el grid  
for _ in range(rows):
    new_row = arr('i', [0] * columns)
    matrix.append(new_row)

# Validando la contruccion del Grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

# Calculando el centro de la primera fila
center = columns // 2

# Estableciendo el centro en 1
matrix[0][center] = 1

# print_matrix(matrix)

# Se calcula el resto de la matrix
# Siguiendo la logica del Sierpinski Gasket
for row in range(1, rows):
    for col in range(columns):
      left_upper_cell = 0
      ringht_upper_cell = 0

      # Si la columna donde estamos 
      # es mayor a 0
      if col > 0:
          left_upper_cell = matrix [row-1] [col-1]
      # Si la columna esta un elemento antes 
      # del borde derecho
      if col < columns - 1:
            ringht_upper_cell = matrix [row-1][col+1]

      # Guardar el arreglo 
      if left_upper_cell != ringht_upper_cell:
         matrix [row][col] = 1
      else:
          matrix [row][col] = 0

print()
print_matrix(matrix) 