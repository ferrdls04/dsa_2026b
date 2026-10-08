"""
Nota:
1. identifico el tamaño de la entrada "n"
El tamaño de la  entrada es el numero de estudiantes.
2.es ver cuanto crece el numero el numero de 
operaciones en mi algoritmo conforme
crece el tamaño de la entrada 
Agrego las bigO identicadas
Teniendo en cuenta la Cota sueperior asintotica
O(n) + O(4) = O(n+4) = O(n)
"""
#creando una lista de estudiantes
students_list_01 = ['Jordan', 'Pipen', 'Curry', 'Shack']
students_list_02 = ['Mike', 'Saul', 'Waiter', 'Jessy']

# Verificado presencia de estudiante
def check_student(input_student, students_list):
    for student in students_list:
       if input_student == student: # 0(n)
           print ("Estudiante encontrado✅") # 0(1)
           return student # 0(1)
    # Si no encuentro al estudiante 
    print ("Estudiante no encontrado❌") # 0(1)
    return None # 0(1)

# Probando algoritmo
check_student("Waiter", students_list_01)

