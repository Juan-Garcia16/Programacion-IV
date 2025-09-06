'''
7. Diseñe una clase `AgendaContactos` con atributos como nombre, teléfono, correo y
dirección. Agregue métodos para buscar contactos, eliminar contactos y actualizar
información desde y hacia un archivo.
'''
class AgendaContactos:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        
    def __str__(self):
        return f"{self.nombre},{self.telefono},{self.correo},{self.direccion}"
    
    def guardar_contacto(self, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            archivo.write(str(self) + "\n")
    
    def buscar_contacto(nombre_archivo, nombre):
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[0].lower() == nombre.lower():
                    return f"Nombre: {datos[0]}, Teléfono: {datos[1]}, Correo: {datos[2]}, Dirección: {datos[3]}"
        return "Contacto no encontrado"
    
    def eliminar_contacto(nombre_archivo, nombre):
        lineas = []
        eliminado = False
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        with open(nombre_archivo, "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0].lower() != nombre.lower():
                    archivo.write(linea)
                else:
                    eliminado = True
        return eliminado
    
    #argumentos con valor por defecto None para evitar actualizar todos los datos de un registro
    def actualizar_contacto(nombre_archivo, nombre, nuevo_telefono = None, nuevo_correo = None, nueva_direccion = None):
        lineas = []
        actualizado = False
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
        
        with open(nombre_archivo, "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0].lower() == nombre.lower():
                    if nuevo_telefono:
                        datos[1] = nuevo_telefono
                    if nuevo_correo:
                        datos[2] = nuevo_correo
                    if nueva_direccion:
                        datos[3] = nueva_direccion
                    actualizado = True
                archivo.write(','.join(datos) + "\n")
        return actualizado

contactos = [
    AgendaContactos("Juan Perez", "1234567895", "juanperez@gmail.com", "Dosquebradas"),
    AgendaContactos("Maria Gomez", "1239050213", "mariagomez@gmail.com", "Avenida del Rio"),
    AgendaContactos("Luis Martinez", "1238941284", "luismartinez@gmail.com", "Centro Pereira"),
    AgendaContactos("Juan Pablo", "1088825664", "juan.garcia16@utp.edu.co", "Pereira"),
    AgendaContactos("Ana Torres", "1234561234", "anatorres@gmail.com", "Manizales"),
    AgendaContactos("Carlos Ruiz", "1237894561", "carlosruiz@gmail.com", "Armenia"),
    AgendaContactos("Sofia Lopez", "1236547890", "sofia.lopez@gmail.com", "Cali")
]

for contacto in contactos:
    contacto.guardar_contacto('agenda_contactos.txt')
    
while True:
    opcion = input("Seleccione una opcion:\n1. Buscar contacto\n2. Eliminar contacto\n3. Actualizar contacto\n4. Salir\n")
    
    if opcion == '1':
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        resultado = AgendaContactos.buscar_contacto('agenda_contactos.txt', nombre_buscar)
        print(f"Resultado de la búsqueda: {resultado}")
        
    elif opcion == '2':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        if AgendaContactos.eliminar_contacto('agenda_contactos.txt', nombre_eliminar):
            print("Contacto eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")
    
    elif opcion == '3':
        nombre_actualizar = input("Ingrese el nombre del contacto a actualizar: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
        nuevo_correo = input("Ingrese el nuevo correo (deje en blanco para no cambiar): ")
        nueva_direccion = input("Ingrese la nueva dirección (deje en blanco para no cambiar): ")
        
        #convertir entradas vacias a None
        nuevo_telefono = nuevo_telefono if nuevo_telefono else None
        nuevo_correo = nuevo_correo if nuevo_correo else None
        nueva_direccion = nueva_direccion if nueva_direccion else None
        
        if AgendaContactos.actualizar_contacto('agenda_contactos.txt', nombre_actualizar, nuevo_telefono, nuevo_correo, nueva_direccion):
            print("Contacto actualizado exitosamente.")
        else:
            print("Contacto no encontrado.")
    
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    
    else:
        print("Opcion no valida. Intente de nuevo")
    

