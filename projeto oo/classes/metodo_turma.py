from buscar import *
from executor_txt import *
from shapes import *
from arquivo_main import *
from salvar_grade import *

class Metodo_busca():

    def metodo_turma(self,codigo):
        classe_cor = Grade()
        procedural_turmas = Salvar_turmas()
        procedural_turmas.tratar_turmas()
        buscar = Buscar_turma(procedural_turmas)   
        turmas_encontradas = buscar.buscar_por_codigo(codigo)
        print('Essas são as suas turmas, com respectivos horários, locais, codigo e semestre.')
        print('Escolha uma turma.')
        lista_turmas = []
        contador_turmas = 0
        for turma in turmas_encontradas:
            contador_turmas += 1
            professor = turma.professor
            horario = turma.horario
            local  = turma.local
            semestre = '2024.2'
            if contador_turmas % 2 ==0:
                print(classe_cor.color_text(f'Há a turma do(a) professor(a) {professor}, seu horário é {horario}, seu local é {local}, e seu semestre é {semestre}------------------{contador_turmas}', "magenta"))
            else:
                print(classe_cor.color_text(f'Há a turma do(a) professor(a) {professor}, seu horário é {horario}, seu local é {local}, e seu semestre é {semestre}------------------{contador_turmas}', "ciano"))
            lista_turmas.append([turma, contador_turmas])
        return lista_turmas


class Metodo_busca_materia():
    
    def metodo_materia_codigo(self,codigo):
            classe_cor = Grade()
            procedural_materias = Salvar_materias()
            procedural_materias.tratar_materia()
            buscar = Buscar_materia(procedural_materias)
            materia = buscar.buscar_por_codigo(codigo)
            if materia:

                print(classe_cor.color_text(f'Encontramos a matéria {materia[0].nome} e o seu código é {materia[0].codigo}', "branco"))
                return materia
                   
            else:
                print("Nenhuma matéria encontrada com esse código.")
                



    def metodo_materia_nome(self,nome):
        classe_cor = Grade()
        procedural_materias = Salvar_materias()
        procedural_materias.tratar_materia()
        buscar = Buscar_materia(procedural_materias)
        contador_nome = 0
        lista_materia = []

        materia_buscada = buscar.buscar_por_nome(nome=nome)
        if materia_buscada:

            for materia in materia_buscada:
                contador_nome += 1
                materia = [materia,contador_nome]
                lista_materia.append(materia)
                if contador_nome % 2 ==0:
                    print(classe_cor.color_text(f'Encontramos a matéria {materia[0].nome} e o seu código é {materia[0].codigo} -------------------- {materia[1]}', "ciano"))
                else:
                    print(classe_cor.color_text(f'Encontramos a matéria {materia[0].nome} e o seu código é {materia[0].codigo} -------------------- {materia[1]}', "magenta"))
                
                if contador_nome == 10:
                    return lista_materia
            return lista_materia
                    
                    
        
        else:
            print("Nenhuma matéria encontrada com esse nome.")
            return lista_materia

class Remover_materia():

    def remover(self, lista_usuario_horario, lista_usuario_materia):
        classe_grade = Grade()
        if lista_usuario_horario == []:
                    print(classe_grade.color_text("Você não pode retirar uma matéria da sua grade, pois não escolheu nenhuma!","vermelho"))
        else:
            print(classe_grade.color_text(f"Essas são as matérias que você possui:","amarelo"))
            contador_cor = 0
            lista_total = []
            lista_voltar_main_materias = []
            lista_voltar_main_horarios = []

            for materia in lista_usuario_horario:
                contador_cor += 1
                append = [materia[0][0], contador_cor]
                lista_total.append(append)
                if contador_cor % 2 == 0:
                    print(classe_grade.color_text(f"{materia[0][0]} ---------- {contador_cor}","magenta"))
                else:
                    print(classe_grade.color_text(f"{materia[0][0]} ---------- {contador_cor}","azul"))

            escolha_exclusao = input(classe_grade.color_text("Digite o número da matéria que deseja excluir -------- ","amarelo"))
            try: 
                escolha_exclusao = int(escolha_exclusao)
            except:
                pass
            if type(escolha_exclusao) == int and len(lista_total) >= escolha_exclusao:
                for numero in lista_total:
                    if numero[1] == escolha_exclusao:
                        continuar =  input(classe_grade.color_text("Você quer continuar com a retirada de matéria?\nSe sim, digite 1\nSe não, digite 2\n","verde"))
                        if continuar == "1":
                            materia = numero[0]
                            for retirar in lista_usuario_materia:
                                if retirar == materia:
                                    pass
                                else:
                                    lista_voltar_main_materias.append(retirar)

                            for retirar in lista_usuario_horario:
                                if materia == retirar[0][0]:
                                    pass
                                else:
                                    lista_voltar_main_horarios.append(retirar)
                            print(classe_grade.color_text(f"Sua matéria {materia} foi retirada com sucesso!","amarelo"))
                            lista_return = lista_voltar_main_horarios+lista_voltar_main_materias
                            return lista_return

                        else:
                            print(classe_grade.color_text("Você optou por não exluir!!","vermelho"))   
                            return 0 
                             

            else:
                print(classe_grade.color_text("Você escolheu uma opção inválida, tente remover novamente!!","vermelho"))   
                return 0 
