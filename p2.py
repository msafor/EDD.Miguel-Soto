class Tarea:
    def __init__(self, identificador, titulo, descripcion, estado):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
class SistemaTareas:
    def __init__(self):
        self.tareas = []
    def agregartarea(self, tarea):
        self.tareas.append(tarea)
    def eliminartarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                self.tareas.remove(tarea)
                break
    def buscartarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                return tarea
        return None
    def cambiarestadotarea(self, identificador, nuevo_estado):
        tarea = self.buscartarea(identificador)
        if tarea:
            tarea.estado = nuevo_estado
    def mostrartareasascendente(self):
        tareasordenadas = sorted(self.tareas, key=lambda tarea: tarea.identificador)
        for tarea in tareasordenadas:
            print(f"Identificador: {tarea.identificador}")
            print(f"Título: {tarea.titulo}")
            print(f"Descripción: {tarea.descripcion}")
            print(f"Estado: {tarea.estado}")
            print()
sistema = SistemaTareas()
#Tareas inventadas
tarea1 = Tarea(3, "Parcial 2", "Realizar 2 ejercicios utilizando la estructura de datos corrrespondiente", "Pendiente")
tarea2 = Tarea(1, "Proyecto", "Realizar un laberinto utilizando pygame", "En progreso")
tarea3 = Tarea(2, "Guia 2", "Realizar 5 ejercicios utilizando la estructura de datos correspondiente", "Completada")
sistema.agregartarea(tarea1)
sistema.agregartarea(tarea2)
sistema.agregartarea(tarea3)
sistema.mostrartareasascendente()
sistema.cambiarestadotarea(2, "Completada")
tareabusqueda = sistema.buscartarea(2)
if tareabusqueda:
    print(f"Parcial 2: {tareabusqueda.titulo}")
else:
    print("Tarea no encontrada")
sistema.eliminartarea(1)
sistema.mostrartareasascendente()
