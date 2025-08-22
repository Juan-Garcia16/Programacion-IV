'''
2. Conteo de palabras en frases
- Diseñe una clase `Frase` con atributos: texto y autor.
- Crea una lista de frases (una lista de objetos, cada objeto va a ser una instancia de
la clase Frase).
- Implemente un método que cuente cuántas veces aparece una palabra clave en
todas las frases.
- Guarde los resultados en `frases.txt`.
'''
class Frase:
    def __init__(self, texto, autor): #constructor para recibir parametros
        self.texto = texto
        self.autor = autor
        
    def cantidad_palabra_clave(palabra, lista_frases):
        cantidad = 0
        for frase in lista_frases:
            palabras = frase.texto.lower().split() 
            cantidad += palabras.count(palabra.lower()) #para asegurar palabras que se repitan en una frase
        return cantidad
        
frases = [Frase("La vida es bella", "Antonio Benitez"),
          Frase("La vuelta al mundo", "Julio verne"),
          Frase("La vuelta a la cuadra", "Anonimo"),
          Frase("Bella julieta", "Romeo")]

palabra_clave = input("Ingrese una palabra: ")
resultado = Frase.cantidad_palabra_clave(palabra_clave, frases)
if resultado > 0:
    archivo = open(r"frases.txt", "w")
    archivo.write(f"la palabra '{palabra_clave}' aparece {resultado} veces en las frases")
    archivo.close()
    print("Se guardaron los resultados en 'frases.txt")
else:
    archivo = open(r"frases.txt", "w")
    archivo.write("La palabra no se encuentra en ninguna frase")
    archivo.close()
    print("Se guardaron los resultados en 'frases.txt")


        