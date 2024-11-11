from shapes import *
from buscar import *
from executor_txt import *
from metodo_turma import *

#iniciando o metodo de salvar e buscar materias
procedural_materias = Salvar_materias()
procedural_materias.tratar_materia()
buscar = Buscar_materia(procedural_materias)

buscar_metodos = Metodo_busca()
buscar_metodos_materia = Metodo_busca_materia()




#iniciando o metodo de salvar e buscar turmas
# procedural_turmas = Salvar_turmas()
# procedural_turmas.tratar_turmas()
# buscar = Buscar_turmas(procedural_turmas)


class Main():
    
    def main(self):
        codigo_pesquisado = ''

        print('Bem vindo ao montador de grade da UnB!!!')
        print('Vamos começar?!')
        print('Para sair do montador digite $.')

        while True:
            metodo = input('''Selecione o método de buscar que prefere:
--------------Por código da matéria: Digite 1
--------------Por nome da matéria: Digite 2
''')
            if metodo == '$':
                print('------------Você desistiu de usar o montador!-------------')
                break
            elif metodo == '1':
                print('---------------Agora iremos pesquisar a sua matéria por código até encontrar.')
                print('Digite "$" para parar de pesquisar')
                
                while True:

                    codigo_pesquisado = input('Digite o código da matéria que deseja.--------- ').lower()
                    
                    if codigo_pesquisado == '$':
                        print('Você desistiu da pesquisa!')
                        break
                    else:
                        buscar_metodos_materia.metodo_materia_codigo(codigo_pesquisado)

            elif metodo == '2':
                print('Agora iremos pesquisar a sua matéria por nome até encontrar.')
                print('Digite "$" para parar de pesquisar')
                while True:
                    nome_pesquisado = input('Digite o nome da matéria que deseja. ').upper()
                    if nome_pesquisado == '$':
                        print('Você desistiu da pesquisa!')
                        break
                    else:
                        materia_buscada = buscar.buscar_por_nome(nome=nome_pesquisado)
                        if materia_buscada:
                            while True:
                                print("Matéria(s) encontrada(s):")
                                contador_nome = 0
                                lista_materia = []
                                for materia in materia_buscada:
                                    contador_nome += 1
                                    materia = [materia,contador_nome]
                                    lista_materia.append(materia)
                                    print(f'Encontramos a matéria {materia[0].nome} e o seu código é {materia[0].codigo} -------------------- {materia[1]}')
                                    if contador_nome == 10:
                                        break

                                verificacao_materias = input('A matéria que você procura está nas opções?'+'\n'+'Se está, digite "S".'+'\n'+'Se não, digite "N". ').upper()
                                #descobrir qual a materia o brother quer
                                if verificacao_materias == 'S':
                                    while True:
                                        escolha_materia = input('Digite o número de sua matéria: ')
                                        try:
                                            escolha_materia = int(escolha_materia)
                                        except:
                                            pass
                                        if type(escolha_materia) == int and  len(lista_materia) >= escolha_materia:
                                            for numero in lista_materia: #numero é igual a lista que criamos
                                                if numero[1] == escolha_materia:
                                                    print(f'A matéria que você escolheu foi {numero[0].nome}')
                                                    print('Agora vamos escolher qual a turma que você deseja.')
                                                    buscar_metodos.metodo_turma(numero[0].codigo)
                                                else:
                                                    pass
                                        
                                        else:
                                            print('Escolha um número que faça parte das matérias que selecionou, caso não tenha, digite "$" para voltar.')
                                            if escolha_materia == '$':
                                                break               
                                else: 
                                    print('Pesquise novamente.')
                                    break
                                                         
                        else:
                            print("Nenhuma matéria encontrada com esse nome.")
                            break

            

            else:
                print('---------------------Método inválido, tente novamente!---------------------')

        
