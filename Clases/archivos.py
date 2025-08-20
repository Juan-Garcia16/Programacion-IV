from io import *

while True:
    opcion=int(input(''' Bienvenido al menu
                        1. Escribir
                        2. Leer
                        3. Borrar
                        4. añadir
                        5. salir
                        Opcion:  '''))
    match opcion:
        case 1:
            archivo=open(r"C:\Users\pipe_\OneDrive\Desktop\archivo.txt","w")
            mensaje=input("ingrese los datos: ")
            archivo.write(f"{mensaje}\n")
            archivo.close()
        case 2:
            archivo=open(r"C:\Users\pipe_\OneDrive\Desktop\archivo.txt","r")
            lectura=archivo.read()
            print(lectura)
            archivo.close()
        case 3:
            archivo=open(r"C:\Users\pipe_\OneDrive\Desktop\archivo.txt","w")
            archivo.close()
        case 4:
            archivo=open(r"C:\Users\pipe_\OneDrive\Desktop\archivo.txt","a")
            mensaje=input("ingrese los datos: ")
            archivo.write(f"{mensaje}\n")
            archivo.close()
        case 5:
            print("adios")
            break