from buscar import *
from executor_txt import *
from shapes import *
from arquivo_main import *


class Metodo_busca():

    def metodo(self,codigo):
        procedural_turmas = Salvar_turmas()
        procedural_turmas.tratar_turmas()
        buscar = Buscar_turma(procedural_turmas)   
        turmas_encontradas = buscar.buscar_por_codigo(codigo)
        print('Essas são as suas turmas, com respectivos horários, locais, codigo e semestre.')
        print('Escolha uma turma.')
        lista_turmas = []
        contador_turmas = 0
        for turma in turmas_encontradas:
            contador_turmas =+ 1
            professor = turma.professor
            horario = turma.horario
            local  = turma.local
            semestre = '2024.2'
            print(f'Há a turma do(a) professor(a) {professor}, seu horário é {horario}, seu local é {local}, e seu semestre é {semestre}------------------{contador_turmas}')
            lista_turmas.append([turma, contador_turmas])
        return turmas_encontradas
