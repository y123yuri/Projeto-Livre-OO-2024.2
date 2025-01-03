from shapes import *
import os
class Salvar_materias():
    def __init__(self):
        self.materias = []  # Lista para armazenar as instâncias de Materia


    def tratar_materia(self):
        with open("projeto oo/arquivos/materias.txt","r", encoding="ISO-8859-1") as leitura:
                for linha in leitura:
                    partes = linha.split('$') 
                    codigo = partes[0].strip() #separa as coisas, nome e codigo
                    nome = partes[1].strip()    
                    
                    classe_materia = Materia(nome=nome,codigo=codigo) #joga na classe
                    self.materias.append(classe_materia)
                    # print(f'joguei {nome} e {codigo} dentro da classe')
        
    def get_materias(self):
            return self.materias #retorna as materias

class Salvar_turmas():
    def __init__(self):
        self.turmas = []

    def tratar_turmas(self):
        with open("projeto oo/arquivos/turmas.txt","r", encoding="ISO-8859-1") as leitura:
                 for linha in leitura:
                    partes = linha.split('$') 
                    codigo = partes[0].strip() #separa as coisas, nome e codigo
                    nome_professor = partes[1].strip() 
                    horario = partes[2].strip()
                    local = partes[3].strip()

                    classe_turma = Turma(professor=nome_professor, local=local, semestre=2024.2, materia=codigo, horario=horario)
                    self.turmas.append(classe_turma)
                    # print(partes)
           
    def get_turmas(self):
            return self.turmas #retorna as turmas
class Limpar():
    import os
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

