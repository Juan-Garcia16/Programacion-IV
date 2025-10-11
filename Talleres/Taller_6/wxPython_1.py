'''
Gestor de Empleados con wxPython y SQLite
Este programa permite agregar, visualizar y gestionar empleados utilizando
una interfaz gráfica básica con xxPython y una base de datos SQLite.
'''

import wx #requiere instalar wxPython: pip install wxPython
import sqlite3

# Base de datos (SQLite)s
def crear_tabla():
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario REAL NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def insertar_empleado(nombre, cargo, salario):
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO empleados (nombre, cargo, salario) VALUES (?, ?, ?)", 
                   (nombre, cargo, salario))
    conexion.commit()
    conexion.close()
    
#quiero eliminar al empleado de id 4
def eliminar_empleado(id):
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM empleados WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
    
eliminar_empleado(4)

def obtener_empleados():
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    conexion.close()
    return empleados


# Interfaz
class VentanaPrincipal(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        self.SetTitle("Gestor de Empleados")
        self.SetSize((500, 400))
        self.Centre()
        
        panel = wx.Panel(self)
        
        # Título
        titulo = wx.StaticText(panel, label="Gestión de Empleados", pos=(160, 15))
        titulo.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        
        # Campos de texto
        wx.StaticText(panel, label="Nombre:", pos=(30, 60))
        self.txt_nombre = wx.TextCtrl(panel, pos=(120, 60), size=(200, -1))
        
        wx.StaticText(panel, label="Cargo:", pos=(30, 100))
        self.txt_cargo = wx.TextCtrl(panel, pos=(120, 100), size=(200, -1))
        
        wx.StaticText(panel, label="Salario:", pos=(30, 140))
        self.txt_salario = wx.TextCtrl(panel, pos=(120, 140), size=(200, -1))
        
        # Botones
        btn_agregar = wx.Button(panel, label="Agregar Empleado", pos=(350, 60))
        btn_agregar.Bind(wx.EVT_BUTTON, self.agregar_empleado) # Evento al hacer clic
        
        btn_actualizar = wx.Button(panel, label="Actualizar Lista", pos=(350, 100))
        btn_actualizar.Bind(wx.EVT_BUTTON, self.mostrar_empleados)
        
        # Lista a mostrar
        self.lista = wx.ListCtrl(panel, pos=(30, 200), size=(440, 150),
                                 style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.lista.InsertColumn(0, "ID", width=40)
        self.lista.InsertColumn(1, "Nombre", width=150)
        self.lista.InsertColumn(2, "Cargo", width=150)
        self.lista.InsertColumn(3, "Salario", width=80)
        
        self.mostrar_empleados() # siempre mostrar al iniciar

    # Métodos funcionales para interactuar con la base de datos
    def agregar_empleado(self, event):
        nombre = self.txt_nombre.GetValue().strip()
        cargo = self.txt_cargo.GetValue().strip()
        salario = self.txt_salario.GetValue().strip()
        
        if not nombre or not cargo or not salario:
            wx.MessageBox("Por favor complete todos los campos.", "Error", wx.ICON_ERROR)
            return
        
        try:
            salario = float(salario)
        except ValueError:
            wx.MessageBox("El salario debe ser un número.", "Error", wx.ICON_ERROR)
            return
        
        insertar_empleado(nombre, cargo, salario)
        wx.MessageBox("Empleado agregado correctamente.", "Éxito", wx.ICON_INFORMATION)
        self.limpiar_campos()
        self.mostrar_empleados()
    
    def mostrar_empleados(self, event=None): # event es opcional
        self.lista.DeleteAllItems()
        empleados = obtener_empleados()
        for emp in empleados:
            index = self.lista.InsertItem(self.lista.GetItemCount(), str(emp[0])) # ID
            self.lista.SetItem(index, 1, emp[1]) # Nombre
            self.lista.SetItem(index, 2, emp[2]) # Cargo
            self.lista.SetItem(index, 3, f"${emp[3]:.2f}") # Salario

    def limpiar_campos(self):
        self.txt_nombre.SetValue("")
        self.txt_cargo.SetValue("")
        self.txt_salario.SetValue("")


# Ejecutar la aplicación
if __name__ == "__main__":
    crear_tabla()
    app = wx.App(False)
    ventana = VentanaPrincipal(None)
    ventana.Show()
    app.MainLoop()
