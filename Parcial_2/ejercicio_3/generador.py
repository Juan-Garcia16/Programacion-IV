import json

def generar_json(direccion_archivo,datos):
    try:
        with open(direccion_archivo,'w') as archivo_json: #abrir archivo en modo escritura
            json.dump(datos,archivo_json,indent=4) #indentacion para mejor lectura en el archivo json
        # print("El archivo se ha generado con exito.")
    except Exception as e: #en caso de error no se para el programa
        print(f"Ocurrio un error: {e}")

def leer_json(direccion_archivo):
    try:
        with open(direccion_archivo,'r') as archivo_json: #abrir archivo en modo lectura
            datos = json.load(archivo_json) #carga el contenido del archivo json y lo convierte en un objeto de python para retornarlo
        return datos
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")
        return None

