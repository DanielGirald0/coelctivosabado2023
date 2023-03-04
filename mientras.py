controladora=100

print("***Empanadas el machetico***")
print("****************************")
print("1. Agregar sabor de empanada")
print("2. Mostrar sabor de empanada")
print("3. Editar sabor de empanada")
print("0.   *SALIR*     ")

while(controladora!=0):
    empanada=None
    controladora=int(input(" Digita una opcion: "))
    if controladora==1:
        empanada=input("Cual es el sabor: ")
    elif controladora==2:
        empanada=input(f"El sabor es: {empanada}")
    elif controladora==3:
        empanada=input("Cual es el sabor: ")
    elif controladora==0:
        empanada=input("Vuelve pronto ")
    else: 
        empanada=input("Opcion invalida")