# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(n)

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students:
        print("se suma 1 total") 
        total += 1 # O(n)
        new_list.append(student) # O(n)
    print("Imprime estudiantes")
    print(new_list) # O(1)
    return total # O(1)

print(f"tamaño de lista: {len(student_list_01)}") # O(1)
print(random_function(student_list_01))
print("")
# Calcular O(2n) + O(5) = O(2n+5) = O(n)
