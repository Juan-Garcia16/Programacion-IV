from clases_ejercicio_2 import Empleado, Proyecto, Junior, Senior, Tester, ProjectManager, LiderTecnico

empleados = []
proyectos = []

j1 = Junior("Ana", 101, "ana@mail.com", "3001234567", "Junior", 3000,
            "Python", "Carlos", "Django")
s1 = Senior("Luis", 102, "luis@mail.com", "3007654321", "Senior", 8000,
            5, "Backend")
t1 = Tester("Marta", 103, "marta@mail.com", "3009998887", "Tester", 4000,
            ["Selenium"], "Automatizada")

p1 = Proyecto("Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"])

pm1 = ProjectManager("Laura", 104, "laura@mail.com", "3011239876", "Project Manager", 12000,
                     "Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"],
                     "Scrum", []) #no se me ocurren reportes, pero seria un campo de descripcion

lt1 = LiderTecnico("Pedro", 105, "pedro@mail.com", "3027654321", "Lider Tecnico", 10000, 8, "Arquitectura",
                   "Sistema de Inventario", "P001", "ClienteX", 50000, 10, ["Ana", "Luis", "Marta"],
                   ["AWS", "Docker"], ["Python", "Kubernetes"])

empleados.extend([j1, s1, t1, pm1, lt1])
proyectos.append(p1)