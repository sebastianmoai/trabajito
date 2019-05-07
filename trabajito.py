#Sebastian Valenzuela
def opcionmenu():
    print("Bienvenido al MENU")
    print("1. Agregar nota")
    print("2. Ver mis notas")
    print("3. Buscar nota especifica")
    print("4. SALIR")
    asd = int(input("Ingrese opción: "))
    while asd<1 or asd>5:
        asd = int(input("La opcion ingresada no es valida "))
    return asd
def agregar_nota ():
    a_nota = []
    n_nota= int(input("ingrese su nueva nota"))
    a_nota.append (n_nota)
    return a_nota
def ver_notas ():
    v_nota = [4.5, 2.3, 5.2, 6.5, 5.8, 3.7, 2.1, 6.5, 4.2, 5.7]
    print("\nLista notas: ",v_nota)
    return v_nota
"""
def buscar_nota (b_nota):
"""
opc=0
while opc!=5:
    opc=opcionmenu():
    if opc==1:
        print ("coloque su nueva nota",agregar_nota())
#no entiendo porque no funciona :(
        
