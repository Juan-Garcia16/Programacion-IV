'''
3. Cadenas clasificadas por vocales
- Crea una clase `Cadena` con un atributo texto.
- Genere una lista de 15 cadenas.
- Implemente un método que ordene primero las cadenas que empiezan con vocal y
luego las demás.
- Guarde la lista ordenada en `cadenas.txt`.
'''

class Cadena:
    def __init__(self, texto):
        self.texto = texto
        
    def orden_por_vocal(lista_cadenas):
        vocales = "aeiou"
        por_vocal = [palabra.texto for palabra in lista_cadenas if palabra.texto[0].lower() in vocales]
        sin_vocal = [palabra.texto for palabra in lista_cadenas if palabra.texto[0].lower() not in vocales]

        por_vocal.sort()
        sin_vocal.sort()
        
        return por_vocal + sin_vocal
        
cadenas = [Cadena('oracle'), Cadena('astro'), Cadena('php') , Cadena('access'), Cadena('electronica'), Cadena('inteligencia'), Cadena('artificial'), Cadena('udemy'), Cadena('platzi'), Cadena('react'), Cadena('angular'), Cadena('unity'), Cadena('python'), Cadena('linux'), Cadena('github')]

lista_ordenada = Cadena.orden_por_vocal(cadenas)
print(lista_ordenada)
archivo = open(r"cadenas.txt", "w")
archivo.write(str(lista_ordenada))
archivo.close()
print("La lista fué guardada en 'cadenas.txt'")

