'''
Selector de Color con wxPython
Este programa muestra un selector de color utilizando wxPython para cambiar 
el color de fondo de la ventana.
'''
import wx

class SelectorColor(wx.Frame):
    def __init__(self, parent, title):
        # directamente al constructor de wx.Frame (sin super)
        wx.Frame.__init__(self, parent, title=title, size=(350, 250))
        panel = wx.Panel(self)
        self.Centre() # centra la ventana en la pantalla

        # Boton para abrir el selector de color
        boton_color = wx.Button(panel, label="Seleccionar color", pos=(90, 80), size=(160, 40))
        boton_color.Bind(wx.EVT_BUTTON, self.elegir_color)

        # se guarda el panel como atributo para poder cambiar su fondo luego
        self.panel = panel

        # mostrar la ventana
        self.Show()

    def elegir_color(self, event):
        dialogo = wx.ColourDialog(self) # crea el dialogo de seleccion de color por defecto

        if dialogo.ShowModal() == wx.ID_OK: # si el usuario presiona OK
            color = dialogo.GetColourData().GetColour()
            self.panel.SetBackgroundColour(color)
            self.panel.Refresh()  # refresca la ventana para aplicar el nuevo color

        dialogo.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    ventana = SelectorColor(None, "Selector de Color - wxPython")
    app.MainLoop()
