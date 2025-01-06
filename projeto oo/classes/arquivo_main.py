from shapes import *
from buscar import *
from executor_txt import *
from metodo_turma import *
from salvar_grade import *
import os
import json



#iniciando o metodo de salvar e buscar materias
procedural_materias = Salvar_materias()
procedural_materias.tratar_materia()
buscar = Buscar_materia(procedural_materias)

buscar_metodos_materia = Metodo_busca_materia()
buscar_metodos = Metodo_busca()
classe_grade = Grade()
remover = Remover_materia()

clear = Limpar()

#iniciando o metodo de salvar e buscar turmas
# procedural_turmas = Salvar_turmas()
# procedural_turmas.tratar_turmas()
# buscar = Buscar_turmas(procedural_turmas)
travador = False


class Main():
    

    def main(self):
        usuario = Usuario(materias=[], turmas_horarios=[])
        lista_salvar_horarios = ""
        codigo_pesquisado = ''

        print(classe_grade.color_text('Bem vindo ao montador de grade da UnB!!!', cor="azul",style=1))
        print(classe_grade.color_text('Vamos começar?!', "verde"))
        print(classe_grade.color_text('Para sair do montador digite $.',"vermelho"))
        nome_usuario = input(classe_grade.color_text('Qual é o seu nome? ','amarelo'))
        if os.path.exists('database_json_usuarios.txt'):
            with open('database_json_usuarios.txt','r', encoding='utf-8') as ler:
                conteudo = json.load(ler)
                if nome_usuario in conteudo.values():
            
                    continuar_grade = input(classe_grade.color_text(f'Bem vindo de volta {nome_usuario}, você já usou o Montador de Grade, Gostaria de continuar com a sua grade antiga?\nSe sim, digite "S".\nSe não, digite "N". ','amarelo')).upper()
                    if continuar_grade == 'S':
                        usuario = Usuario(materias=conteudo['nomes_materias'], turmas_horarios=conteudo['turmas_e_horarios'])
                    else:
                        print(classe_grade.color_text('Tudo ótimo, pode recriar as suas grades do zero!', 'magenta'))
                        
                
                else:
                    print(classe_grade.color_text(f'Seja Bem vindo, {nome_usuario}!\nAcho que é a sua primeira vez usando o Montador de Grade!!!!\nAproveite!','amarelo'))
                    pass

                        
        else:
            print(classe_grade.color_text(f'Seja Bem vindo, {nome_usuario}!\nAcho que é a sua primeira vez usando o Montador de Grade!!!!\nAproveite!','amarelo'))
        while True:
            travador = False
            metodo_escolha = input(classe_grade.color_text("Gostaria de ver como está sua grade? --------- Digite 1\nGostaria de remover uma matéria? --------- Digite 2\nGostaria de adicionar uma matéria? --------- Digite 3\nGostaria de sair do programa? --------- Digite $\n","verde")).upper()
            if metodo_escolha == "1":
                # print(usuario.turmas_horarios)
                clear.clear_terminal()
                classe_grade.exibir_grade(lista_recebida=usuario.turmas_horarios)
                

            elif metodo_escolha == "2":
                # clear.clear_terminal()
                lista_return = remover.remover(lista_usuario_horario=usuario.turmas_horarios, lista_usuario_materia=usuario.materias)
                if lista_return == '':
                    pass  
                else:
                    
                    usuario.turmas_horarios = lista_return[0]
                    usuario.materias = lista_return[1]
  

            elif metodo_escolha == "3":
                clear.clear_terminal()

                metodo = input(classe_grade.color_text('''Selecione o método de buscar que prefere:
--------------Por código da matéria digite "1".
--------------Por nome da matéria digite "2".
''', "amarelo"))
                
                if metodo == '$':
                    print(classe_grade.color_text('------------Você desistiu de usar o montador!-------------',"vermelho"))
                    break
                elif metodo == '1':
                    print(classe_grade.color_text('---------------Agora iremos pesquisar a sua matéria por código até encontrar.',"verde"))
                    print(classe_grade.color_text('Digite "$" para parar de pesquisar',"vermelho"))
                    
                    while True:
                        if travador == True:
                            break

                        codigo_pesquisado = input(classe_grade.color_text('Digite o código da matéria que deseja.--------- ',"verde")).upper().strip()
                        
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
                                    verificacao_turma = input(classe_grade.color_text('A turma que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ', "verde")).upper() 
                                    
                                    if verificacao_turma == 'S':
                                        while True:
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
                                                    if travador == True:
                                                        break
                                                    if numero[1] == escolha_turma:
                                                        leitor = classe_grade.leitor(numero[0].horario) #chama a classe grade para decifrar o horario
                                                
                                                        print_turma = classe_grade.printar_na_main_turma(nome_materia=materia[0].nome, professor=numero[0].professor, dia=leitor[0], hora=leitor[1], local=numero[0].local, horario_unb=numero[0].horario)
                                                        adicionar_na_grade = input(classe_grade.color_text('Você gostaria de adicionar essa turma a sua grade?\nSe sim, digite "S"\nSe não, digite "N" ',"azul")).upper()
                                                        if adicionar_na_grade == "S":
                                                            if usuario.turmas_horarios != []:
                                                                lista_info_turma = [[materia[0].nome, materia[0].codigo], leitor[0]]

                                                                variavel_travamento = classe_grade.verificacao(lista_info_turma=lista_info_turma, usuario_materias=usuario.materias, usuario_turma_horarios=usuario.turmas_horarios)
        
                                                                if variavel_travamento == 1:
                                                                    travador = True
                                                                    break #esse break é importante

                                                                lista_antiga_turmas_horarios = usuario.turmas_horarios
                                                                lista_antiga_materia = usuario.materias
                                                                lista_antiga_turmas_horarios.append(lista_info_turma)
                                                                lista_antiga_materia.append(materia[0].nome)
                                                                usuario = Usuario(materias=lista_antiga_materia, turmas_horarios=lista_antiga_turmas_horarios)

                                                            else:
                                                                lista_info_turma = [[[materia[0].nome, materia[0].codigo], leitor[0]]]
                                                                usuario = Usuario(materias=[materia[0].nome], turmas_horarios=lista_info_turma)                                                        
                                        

                                                            print(classe_grade.color_text(f"Você adicinou a matéria {materia[0].nome} com o professor {numero[0].professor}!","amarelo"))
                                                            travador = True
                                                
                                                            break
                                                                                
                                                        else:
                                                            print(classe_grade.color_text("Opção inválida!","vermelho"))
                                                            break
                                                    else:
                                                        pass
                                            else:
                                                pass
                                    else:
                                        print('Você digitou não, pesquise novamente.')
                                else:
                                    print('Opção inválida, pesquise novamente.')
                                    break   
                            

                elif metodo == '2':
                    print(classe_grade.color_text('Agora iremos pesquisar a sua matéria por nome até encontrar.',"verde"))
                    print(classe_grade.color_text('Digite "$" para parar de pesquisar',"vermelho"))
                    while True:
                        if travador == True:
                            break
                        nome_pesquisado = input(classe_grade.color_text('Digite o nome da matéria que deseja. ',"branco")).upper().strip()
                        if nome_pesquisado == '$':
                            print('Você desistiu da pesquisa!')
                            break
                        else:
                                lista_materia = buscar_metodos_materia.metodo_materia_nome(nome_pesquisado)
                                
                                
                                if not lista_materia : # 
                                    pass

                                else:
                                    verificacao_materias = input(classe_grade.color_text('A matéria que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ', "33")).upper()
                                    #descobrir qual a materia o brother quer
                                    if verificacao_materias == 'S':
                                        while True:
                                            if travador == True:
                                                break
                                            print('Caso queira sair, digite "$".')
                                            escolha_materia = input(classe_grade.color_text('Digite o número de sua matéria: ',"azul"))
                                            try:
                                                escolha_materia = int(escolha_materia)
                                            except:
                                                if escolha_materia == '$':
                                                    break
                                                pass
                                            if type(escolha_materia) == int and  len(lista_materia) >= escolha_materia:
                                                for materia in lista_materia: #numero é igual a lista que criamos
                                                    if materia[1] == escolha_materia:
                                                        print(classe_grade.color_text(f'A matéria que você escolheu foi {materia[0].nome}',"magenta"))
                                                        print(classe_grade.color_text('Agora vamos escolher qual a turma que você deseja.',"amarelo"))
                                                        lista_turmas = buscar_metodos.metodo_turma(materia[0].codigo)
                                                        verificacao_turma = input(classe_grade.color_text('A turma que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ',"verde")).upper()
                                                        
                                                        if verificacao_turma == 'S':
                                                        
                                                            while True:
                                        
                                                                if travador == True:
                                                                    break
                                                                print(classe_grade.color_text('Caso queira sair, digite "$".',"vermelho"))
                                                                escolha_turma = input(classe_grade.color_text('Digite o número de sua turma: ',"amarelo"))
                                                                try:
                                                                    escolha_turma = int(escolha_turma)
                                                                except:
                                                                    if escolha_turma == '$':
                                                                        break
                                                                    pass
                                                                if type(escolha_turma) == int and  len(lista_turmas) >= escolha_turma:
                                                                    for numero in lista_turmas: #numero é igual a lista que criamos
                                                                        if travador == True:
                                                                            break
                                                                        if numero[1] == escolha_turma:
                                                                            leitor = classe_grade.leitor(numero[0].horario) #chama a classe grade para decifrar o horario
                                                                        
                                                                            print_turma = classe_grade.printar_na_main_turma(nome_materia=materia[0].nome, professor=numero[0].professor, hora=leitor[1], dia=leitor[0], local=numero[0].local, horario_unb=numero[0].horario)
                                                                            adicionar_na_grade = input(classe_grade.color_text('Você gostaria de adicionar essa turma a sua grade?\nSe sim, digite "S"\nSe não, digite "N" ',"azul")).upper()
                                                                            if adicionar_na_grade == "S":
                                                                                if usuario.turmas_horarios != []:
                                                                                    lista_info_turma = [[materia[0].nome, materia[0].codigo], leitor[0]]

                                                                                    variavel_travamento = classe_grade.verificacao(lista_info_turma=lista_info_turma, usuario_materias=usuario.materias, usuario_turma_horarios=usuario.turmas_horarios)
                            
                                                                                    if variavel_travamento == 1:
                                                                                        travador = True
                                                                                        break #esse break é importante

                                                                                    lista_antiga_turmas_horarios = usuario.turmas_horarios
                                                                                    lista_antiga_materia = usuario.materias
                                                                                    lista_antiga_turmas_horarios.append(lista_info_turma)
                                                                                    lista_antiga_materia.append(materia[0].nome)
                                                                                    usuario = Usuario(materias=lista_antiga_materia, turmas_horarios=lista_antiga_turmas_horarios)

                                                                                else:
                                                                                    lista_info_turma = [[[materia[0].nome, materia[0].codigo], leitor[0]]]
                                                                                    usuario = Usuario(materias=[materia[0].nome], turmas_horarios=lista_info_turma)                                                        
                                                            

                                                                                print(classe_grade.color_text(f"Você adicinou a matéria {materia[0].nome} com o professor {numero[0].professor}!","amarelo"))
                                                                                travador = True
                                                                                
                                                                            
                                                                                break
                                                                                
                                                                            else:
                                                                                print(classe_grade.color_text("Você escolheu a opção negativa, procure novamente!","vermelho"))
                                                                                travador = True
                                                                                break
                                                                        else:
                                                                            pass
                                                                else:
                                                                    pass
                                                        else:
                                                            print('Você digitou não, pesquise novamente.')    
                                                    else: 
                                                        pass
                                            
                                            else:
                                                print('Escolha um número que faça parte das matérias que selecionou, caso não tenha, digite "$" para voltar.')
                                                if escolha_materia == '$':
                                                    break               
                                    else: 
                                        print('Pesquise novamente.')
                                        break

            elif metodo_escolha == "$":
                if os.path.exists('database_json_usuarios.txt'):
                    os.remove('database_json_usuarios.txt')
                else:
                    pass #nao existe o arquivo

                if not os.path.exists('database_json_usuarios.txt') and usuario.turmas_horarios != [] and usuario.materias != []:
                    banco_usuario = {
                        'usuario_banco' : nome_usuario,
                        'turmas_e_horarios' : usuario.turmas_horarios,
                        'nomes_materias' : usuario.materias

                    }
                    with open('database_json_usuarios.txt','w',encoding='utf-8') as criar:
                        json.dump(banco_usuario, criar, ensure_ascii=False ,indent=4)
                    print(classe_grade.color_text('Sua grade está salva em nosso banco de dados para caso queira ver-la novamente depois!','verde'))
                else:
                    pass
                print(classe_grade.color_text("Obrigado por usar o montador de grade!!","amarelo"))
                

                break

            else:
                print(classe_grade.color_text("Opção inválida!","vermelho"))

        
