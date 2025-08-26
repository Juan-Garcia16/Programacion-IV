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

    def registrar_eventos(eventos, archivo = "agenda.txt"):
        archivo = open(archivo, "w")
        for evento in eventos:
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

        

eventos = [
    Evento("Concierto de Rock", "2025-09-07", "20:00", "Estadio Nacional", "Carlos Pérez"),
    Evento("Feria del Libro", "2025-09-05", "10:00", "Centro de Convenciones", "Ana Torres"),
    Evento("Maratón Ciudad", "2025-11-01", "06:30", "Parque Principal", "Luis Gómez"),
    Evento("Congreso de Tecnología", "2025-08-30", "09:00", "Hotel Intercontinental", "María Rodríguez"),
    Evento("Obra de Teatro: Hamlet", "2025-09-03", "19:30", "Teatro Central", "Pedro Ramírez"),
    Evento("Taller de Fotografía", "2025-09-12", "15:00", "Casa de la Cultura", "Laura Sánchez")
]
        
Evento.registrar_eventos(eventos)
Evento.eventos_proxima_semana()