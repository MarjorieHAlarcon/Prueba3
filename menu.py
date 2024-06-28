import funciones

def menuprincipal():
    print('***************************')
    print ('** M U N D O   L I B R O **')
    print ('****************************')
    print ('[1] Mantenedor de categorias ')
    print ('[2]  Reportes ')
    print ('[3]   Salir       ')
    
opc=int(input("Seleccione una opcion "))

if opc == 1:
     menu_mantenedores()
elif opc == 2:
    reportes()
elif opc == 3:
    int(input('Salir '))



def menu_mantenedores():
    print('******************')
    print ('** Mantenedor Categorias **')
    print ('[1] Editar Categoria ')
    print ('[2] Buscar categoria ')
    print ('[3] Eliminar categoria ')
    print ('[4] Agregar categoria ')
    print ('[5] Salir ')

def reportes():
    print ('*********************')
    print ('** LIBRO                Cantidad de veeces prestado')

