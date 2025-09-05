'''
8. Agenda de eventos
- Crea una clase `Evento` con atributos: título, fecha, hora, lugar y responsable.
- Permita registrar varios eventos y guardarlos en `agenda.txt`.
- Implemente un método que lea el archivo y muestre solo los eventos programados
para la próxima semana.
'''
class Evento:
    def __init__(self, titulo, fecha, hora, lugar, responsable):
        self.titulo = titulo
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.responsable = responsable
    
    def __str__(self):
        return f"{self.titulo},{self.fecha},{self.hora},{self.lugar},{self.responsable}"

    def registrar_evento(archivo = "agenda.txt"):
        titulo = input("Ingrese el título del evento: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        lugar = input("Ingrese el lugar: ")
        responsable = input("Ingrese el responsable: ")

        evento = Evento(titulo, fecha, hora, lugar, responsable)
        
        archivo = open(archivo, "a")
        archivo.write(str(evento) + "\n")
        archivo.close()
        
    def eventos_proxima_semana(archivo = "agenda.txt"):
        archivo = open(archivo, "r")
        print("Eventos próxima semana:")
        for linea in archivo:
            datos = linea.strip().split(",")
            titulo = datos[0]
            fecha = datos[1]
            lista_fecha = fecha.split("-")
            #semana siguiete actual
            if (lista_fecha[1] == "09") and (1 <= int(lista_fecha[2]) <=7 ):
                print(f"{titulo}: {fecha}")

    
while True:
    print("\n1. Registrar un evento")
    print("2. Ver eventos de la próxima semana")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Evento.registrar_evento()
    elif opcion == "2":
        Evento.eventos_proxima_semana()
    elif opcion == "3":
        print("Saliendo del programa")
        break
    else:
        print("Opción no valida, intente de nuevo")