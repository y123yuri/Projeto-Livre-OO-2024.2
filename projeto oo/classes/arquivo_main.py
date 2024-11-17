from shapes import *
from buscar import *
from executor_txt import *
from metodo_turma import *
from salvar_grade import *

#iniciando o metodo de salvar e buscar materias
procedural_materias = Salvar_materias()
procedural_materias.tratar_materia()
buscar = Buscar_materia(procedural_materias)

buscar_metodos_materia = Metodo_busca_materia()
buscar_metodos = Metodo_busca()
classe_grade = Grade()



#iniciando o metodo de salvar e buscar turmas
# procedural_turmas = Salvar_turmas()
# procedural_turmas.tratar_turmas()
# buscar = Buscar_turmas(procedural_turmas)
travador = False


class Main():
    
    def main(self):
        usuario = Usuario(materias=[], turmas_horarios=[])

        codigo_pesquisado = ''

        print(classe_grade.color_text('Bem vindo ao montador de grade da UnB!!!', cor="azul",style=1))
        print(classe_grade.color_text('Vamos começar?!', "verde"))
        print(classe_grade.color_text('Para sair do montador digite $.',"vermelho"))

        while True:
            travador = False
            ver_grade = input(classe_grade.color_text("Gostaria de ver como está sua grade?\n Se sim, digite 'S'.\n Se não, digite 'N'\n","verde")).upper()
            if ver_grade == "S":
                print(usuario.turmas_horarios)
                classe_grade.exibir_grade(lista_recebida=usuario.turmas_horarios)
            else:
                pass
            metodo = input(('''Selecione o método de buscar que prefere:
--------------Por código da matéria digite "1".
--------------Por nome da matéria digite "2".
'''))
            if metodo == '$':
                print(classe_grade.color_text('------------Você desistiu de usar o montador!-------------',"vermelho"))
                break
            elif metodo == '1':
                print(classe_grade.color_text('---------------Agora iremos pesquisar a sua matéria por código até encontrar.',"verde"))
                print(classe_grade.color_text('Digite "$" para parar de pesquisar',"vermelho"))
                
                while True:

                    codigo_pesquisado = input('Digite o código da matéria que deseja.--------- ').upper()
                    
                    if codigo_pesquisado == '$':
                        print(classe_grade.color_text('Você desistiu da pesquisa!',"vermelho"))
                        break
                    else:
                        materia = buscar_metodos_materia.metodo_materia_codigo(codigo_pesquisado)
                        if not materia:
                            pass
                        else:
                            verificacao_codigo = input('A matéria que você procura está correta?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ').upper()
                            if verificacao_codigo == 'S':
                                print(f'A matéria que você escolheu foi {materia[0].nome}')
                                print('Agora vamos escolher qual a turma que você deseja.')
                                lista_turmas = buscar_metodos.metodo_turma(materia[0].codigo)
                                verificacao_turma = input('A turma que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ').upper() 
                                
                                if verificacao_turma == 'S':
                                    while True:
                                        print('Caso queira sair, digite "$".')
                                        escolha_turma = input('Digite o número de sua turma: ')
                                        try:
                                            escolha_turma = int(escolha_turma)
                                        except:
                                            if escolha_turma == '$':
                                                break
                                            pass
                                        if type(escolha_turma) == int and  len(lista_turmas) >= escolha_turma:
                                            for numero in lista_turmas: #numero é igual a lista que criamos
                                                if numero[1] == escolha_turma:
                                                    leitor = classe_grade.leitor(numero[0].horario) #chama a classe grade para decifrar o horario
                                            
                                                    print_turma = classe_grade.printar_na_main_turma(nome_materia=materia[0].nome, professor=numero[0].professor, hora=leitor[2], dias=leitor[0], local=numero[0].local, horario_unb=numero[0].horario)
                                                else:
                                                    pass
                                        else:
                                            pass
                                else:
                                    print('Opção inválida, pesquise novamente.')
                            else:
                                print('Opção inválida, pesquise novamente.')
                                break   
                        

            elif metodo == '2':
                print('Agora iremos pesquisar a sua matéria por nome até encontrar.')
                print('Digite "$" para parar de pesquisar')
                while True:
                    if travador == True:
                        break
                    nome_pesquisado = input('Digite o nome da matéria que deseja. ').upper()
                    if nome_pesquisado == '$':
                        print('Você desistiu da pesquisa!')
                        break
                    else:
                            lista_materia = buscar_metodos_materia.metodo_materia_nome(nome_pesquisado)
                            
                            
                            if not lista_materia : # 
                                pass

                            else:
                                verificacao_materias = input('A matéria que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ').upper()
                                #descobrir qual a materia o brother quer
                                if verificacao_materias == 'S':
                                    while True:
                                        if travador == True:
                                            break
                                        print('Caso queira sair, digite "$".')
                                        escolha_materia = input('Digite o número de sua matéria: ')
                                        try:
                                            escolha_materia = int(escolha_materia)
                                        except:
                                            if escolha_materia == '$':
                                                break
                                            pass
                                        if type(escolha_materia) == int and  len(lista_materia) >= escolha_materia:
                                            for materia in lista_materia: #numero é igual a lista que criamos
                                                if materia[1] == escolha_materia:
                                                    print(f'A matéria que você escolheu foi {materia[0].nome}')
                                                    print('Agora vamos escolher qual a turma que você deseja.')
                                                    lista_turmas = buscar_metodos.metodo_turma(materia[0].codigo)
                                                    verificacao_turma = input('A turma que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ').upper()
                                                     
                                                    if verificacao_turma == 'S':
                                                    
                                                        while True:
                                                            print(travador)
                                                            if travador == True:
                                                                break
                                                            print('Caso queira sair, digite "$".')
                                                            escolha_turma = input('Digite o número de sua turma: ')
                                                            try:
                                                                escolha_turma = int(escolha_turma)
                                                            except:
                                                                if escolha_turma == '$':
                                                                    break
                                                                pass
                                                            if type(escolha_turma) == int and  len(lista_turmas) >= escolha_turma:
                                                                for numero in lista_turmas: #numero é igual a lista que criamos
                                                                    if numero[1] == escolha_turma:
                                                                        leitor = classe_grade.leitor(numero[0].horario) #chama a classe grade para decifrar o horario
                                                                    
                                                                        print_turma = classe_grade.printar_na_main_turma(nome_materia=materia[0].nome, professor=numero[0].professor, hora=leitor[2], dias=leitor[0], local=numero[0].local, horario_unb=numero[0].horario)
                                                                        adicionar_na_grade = input(classe_grade.color_text("Você gostaria de adicionar essa matéria a sua grade? ","azul")).upper()
                                                                        if adicionar_na_grade == "S":
                                                                            lista_info_turma = [[[materia[0].nome], leitor[0], leitor[1]]]
                                                                            usuario = Usuario(materias=[materia[0].nome], turmas_horarios=lista_info_turma)
                                                                            print(usuario.turmas_horarios)
                                                                            print(classe_grade.color_text("Você escolheu uma matéria!","amarelo"))
                                                                            travador = True
                                                                            print(travador)
                                                                            break
                                                                            
                                                                        else:
                                                                            break
                                                                    else:
                                                                        pass
                                                            else:
                                                                pass
                                                    else:
                                                        print('Opção inválida, pesquise novamente.')    
                                                else: 
                                                    pass
                                        
                                        else:
                                            print('Escolha um número que faça parte das matérias que selecionou, caso não tenha, digite "$" para voltar.')
                                            if escolha_materia == '$':
                                                break               
                                else: 
                                    print('Pesquise novamente.')
                                    break
                            
                                                         
                      
            

                # print('---------------------Método inválido, tente novamente!---------------------')

        
