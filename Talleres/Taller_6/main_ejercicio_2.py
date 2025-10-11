import json
from objetos_ejercicio_2 import empleados, proyectos, j1, s1, t1, pm1, lt1, p1


print("\n--- INFORMACION EMPLEADOS ---")
for e in empleados:
    e.mostrar_informacion()

print("\n--- STACK JUNIORS ---")
j1.mostrar_stack()

print("\n--- SALARIO SENIORS ---")
print(f"Salario total de {s1.get_nombre()}: {s1.calcular_salario_total()}")

print("\n--- DIAGNOSTICO TESTER ---")
t1.ejecutar_prueba()

print("\n--- INFORMACION PROYECTO ---")
p1.mostrar_proyecto()
print(f"Costo mensual: {p1.costo_mensual()}")

print("\n--- REPORTE PROJECT MANAGER ---")
pm1.generar_reporte("Sprint 1 completado exitosamente")

print("\n--- TECNOLOGIAS DEL LIDER TECNICO ---")
lt1.listar_tecnologias()


def guardar_lista_json(lista_objetos, nombre_archivo):
    datos = [obj.to_dict() for obj in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

guardar_lista_json(empleados, "empleados.json")
guardar_lista_json(proyectos, "proyectos.json")
print("\n\nDatos guardados en empleados.json y proyectos.json")