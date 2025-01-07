from shapes import *
import os

import os
from shapes import *

class Salvar_materias():
    def __init__(self):
        self.materias = []  

    def tratar_materia(self):
        # Determina o diretório base dinamicamente
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "arquivos", "materias.txt")  

        with open(file_path, "r", encoding="ISO-8859-1") as leitura:
            for linha in leitura:
                partes = linha.split('$')
                codigo = partes[0].strip()  # separa as coisas, nome e código
                nome = partes[1].strip()

                classe_materia = Materia(nome=nome, codigo=codigo)  # joga na classe
                self.materias.append(classe_materia)

    def get_materias(self):
        return self.materias  # Retorna as matérias


class Salvar_turmas():
    def __init__(self):
        self.turmas = []

    def tratar_turmas(self):
        # Determina o diretório base dinamicamente
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "arquivos", "turmas.txt")  # Caminho absoluto para turmas.txt

        with open(file_path, "r", encoding="ISO-8859-1") as leitura:
            for linha in leitura:
                partes = linha.split('$')
                codigo = partes[0].strip()  # separa as coisas, nome e código
                nome_professor = partes[1].strip()
                horario = partes[2].strip()
                local = partes[3].strip()

                classe_turma = Turma(professor=nome_professor, local=local, semestre=2024.2, materia=codigo, horario=horario)
                self.turmas.append(classe_turma)

    def get_turmas(self):
        return self.turmas  # Retorna as turmas

class Limpar():
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
# class Salvar_materias():
#     def __init__(self):
#         self.materias = []  # Lista para armazenar as instâncias de Materia


#     def tratar_materia(self):
#         with open("projeto oo/arquivos/materias.txt","r", encoding="ISO-8859-1") as leitura:
#                 for linha in leitura:
#                     partes = linha.split('$') 
#                     codigo = partes[0].strip() #separa as coisas, nome e codigo
#                     nome = partes[1].strip()    
                    
#                     classe_materia = Materia(nome=nome,codigo=codigo) #joga na classe
#                     self.materias.append(classe_materia)
#                     # print(f'joguei {nome} e {codigo} dentro da classe')
        
#     def get_materias(self):
#             return self.materias #retorna as materias

# class Salvar_turmas():
#     def __init__(self):
#         self.turmas = []

#     def tratar_turmas(self):
#         with open("projeto oo/arquivos/turmas.txt","r", encoding="ISO-8859-1") as leitura:
#                  for linha in leitura:
#                     partes = linha.split('$') 
#                     codigo = partes[0].strip() #separa as coisas, nome e codigo
#                     nome_professor = partes[1].strip() 
#                     horario = partes[2].strip()
#                     local = partes[3].strip()

#                     classe_turma = Turma(professor=nome_professor, local=local, semestre=2024.2, materia=codigo, horario=horario)
#                     self.turmas.append(classe_turma)
#                     # print(partes)
           
#     def get_turmas(self):
#             return self.turmas #retorna as turmas
# class Limpar():
#     import os
#     def clear_terminal(self):
#         os.system('cls' if os.name == 'nt' else 'clear')

