class Pencil:
    def __init__(self, x="black"):
        self.__cor = x
    
    def escrever(self,txt):
        print(f'minha cor é {self.__cor} e o txt é {txt}')
    
    def get_cor(self):
        return self.__cor
    