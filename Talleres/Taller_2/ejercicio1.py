'''
1. Números y dígitos invertidos
- Crear una clase `Numero` donde pueda tener un entero de tres cifras.
- Implemente un método que devuelva la suma de sus dígitos.
- Implemente otro método que escriba en `numeros.txt` el número original y su versión
invertida.
- Leer el archivo e imprimir los resultados.
'''
class Numero:
    num = 0
    
    def suma_digitos(self):
        suma = 0
        num = str(self.num)
        for digito in num:
            suma += int(digito)
        print(f"\nSuma de los digitos: {suma}")
        
    def escribir_archivo(self):
        num_texto = str(self.num)
        num_invertido = "".join(reversed(num_texto)) #necesario el join porque reversed devuelve un objeto
        
        archivo = open(r"numeros.txt", "w")
        archivo.write(f"Original: {num_texto}\n")
        archivo.write(f"Invertido: {num_invertido}\n")
        archivo.close()

num_tres_cifras = Numero()
num_tres_cifras.num = int(input("Ingrese un número de 3 cifras: "))
num_tres_cifras.suma_digitos()
num_tres_cifras.escribir_archivo()
            
archivo = open(r"numeros.txt", "r")
lectura = archivo.read()
print(lectura)