class Video:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion
class Nodo:
    def __init__(self, video):
        self.video = video
        self.siguiente = None
class ListaReproduccion:
    def __init__(self):
        self.primero = None
    def estavacia(self):
        return self.primero is None
    def agregarvideo(self, video):
        nnodo = Nodo(video)
        if self.estavacia():
            self.primero = nnodo
            nnodo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nnodo
            nnodo.siguiente = self.primero
    def mostrarlista(self):
        if self.estavacia():
            print("La lista de reproducción está vacía.")
        else:
            actual = self.primero
            while True:
                print("Título:", actual.video.titulo)
                print("Autor:", actual.video.autor)
                print("Duración:", actual.video.duracion)
                print("---------------")
                actual = actual.siguiente
                if actual == self.primero:
                    break
    def buscarvideo(self, titulo):
        if self.estavacia():
            print("La lista está vacía.")
            return None
        actual = self.primero
        while True:
            if actual.video.titulo == titulo:
                return actual.video
            actual = actual.siguiente
            if actual == self.primero:
                break
        print("El video no se encontra en la lista.")
        return None
    def eliminarvideo(self, titulo):
        if self.estavacia():
            print("La lista de reproducción está vacía.")
            return
        actual = self.primero
        anterior = None
        encontrado = False
        while True:
            if actual.video.titulo == titulo:
                if actual == self.primero:
                    ultimo = self.primero
                    while ultimo.siguiente != self.primero:
                        ultimo = ultimo.siguiente
                    self.primero = actual.siguiente
                    ultimo.siguiente = self.primero
                else:
                    anterior.siguiente = actual.siguiente
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.primero:
                break
        if encontrado:
            print("Video eliminado correctamente.")
        else:
            print("El video no se encuentra en la lista.")
Lista=ListaReproduccion()
#Videos no reales los inventé yo
pvideo= Video("Grandes Aventuras","Esteban Armados","10;45")
svideo= Video("El final de la batalla","Miguel Soto","25:40")
tvideo= Video("Mi primer video", "Luis Rios", "9:28")
cvideo= Video("La batalla final","Kevin Urrutia", "35:12")
Lista.agregarvideo(pvideo)
Lista.agregarvideo(svideo)
Lista.agregarvideo(tvideo)
Lista.agregarvideo(cvideo)
Lista.mostrarlista()
Lista.buscarvideo("pvideo")
Lista.buscarvideo("El final de la batalla")
Lista.eliminarvideo("Grandes Aventuras")
Lista.mostrarlista()






