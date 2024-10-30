class Point:
    def __init__(self, x, y):
        self.set(x, y)

    def set(self, x, y):
        if isinstance(x, int) or isinstance(x, float):
            self._x = x 
        else:
            self._x = 0
            print('Seu x foi definido como 0, porque você não colocou um int ou float, tente novamente')
        if isinstance(y, int) or isinstance(y, float):
            self._y = y 
        else:
            self._y = 0
            print('Seu y foi definido como 0, porque você não colocou um int ou float, tente novamente')

    def distance(self):
        return (self._x ** 2 + self._y  ** 2) ** (0.5)

    def get_x(self):
        return self._x

    def get_y(self):
        return self.y



class Circulo(Point): # HERANÇA
    def __init__ (self, x, y, r):
        super().__init__(x, y)
        self._r = r
    def interferencia(self, ponto):
        pass
    def imprimir(self):
        print(f'Eu sou um circulo e tenho uma origem em ({self._x},{self._y}). Meu raio é {self._r}')