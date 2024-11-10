from shapes import *

class Buscar_materia():
    def __init__(self, salvar_instance):
        self.materias = salvar_instance.get_materias()  # Obtem a lista de objetos Materia

    def buscar_por_nome(self, nome):
        return [materia for materia in self.materias if nome.lower() in materia.nome.lower()] #usa o lower pra deixar tudo na mesma forma, e busca dentro da lista

    def buscar_por_codigo(self, codigo):
        return [materia for materia in self.materias if codigo.lower() == materia.codigo.lower()] #usa o lower pra deixar tudo na mesma forma, e busca dentro da lista

class Buscar_turma():
    def __init__(self, salvar_instance):
        self.turmas = salvar_instance.get_turmas() 

    def buscar_por_codigo(self, codigo):
        return [turma for turma in self.turmas if turma.materia.lower() == codigo.lower()]