class Aprender():
    def __init__(self, x):
        self._x = x

    def __str__(self):
        return f"Objeto Aprender com valor: {self._x}"
    
obj = Aprender("A")
print(obj)  # Isso imprimirá "Objeto Aprender com valor: A"
