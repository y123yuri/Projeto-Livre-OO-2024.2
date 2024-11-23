class Grade():
    def leitor(self,codigo_horario):
        blocos = codigo_horario.split()

        printar_main_geral = []

        lista_horarios_reais = [[2, "Segunda"], [3, "Terça"], [4, "Quarta"], [5, "Quinta"], [6, "Sexta"], [7, "Sábado"]]
        lista_horarios_feitos = [["M1", "08:00 - 09:00"], ["M2", "09:00 - 09:50"], ["M3", "10:00 - 11:00"], ["M4", "11:00 - 11:50"],
                                ["M5", "12:00 - 13:00"], ["T1", "13:00 - 13:50"], ["T2", "14:00 - 15:00"], ["T3", "15:00 - 15:50"],
                                ["T4", "16:00 - 17:00"], ["T5", "17:00 - 17:50"], ["N1", "19:00 - 19:50"], ["N2", "19:50 - 20:40"],
                                ["N3", "20:50 - 21:40"], ["N4", "21:40 - 22:30"]]
        lista_turno = [["M", "Matutino"], ["T", "Vespertino"], ["N", "Noturno"]]
        dicionario_horarios = {}

        # Processar cada bloco de código
      
            
        for bloco in blocos:
            dias = []
            horarios = []
            printar_main = []
            letra_turno = ""

            for letra in bloco:  
                if letra.isdigit():
                    if letra_turno:  # Já identificamos o turno
                        numero_mais_turno = f"{letra_turno}{letra}"  # Ex: T3, M1

                        for horario in lista_horarios_feitos:
                            if horario[0] == numero_mais_turno:
                                horarios.append(horario[0])  # Adiciona horário formatado (08:00 - 09:00, etc)
                                printar_main.append(horario[1])
                    else:  # Ainda estamos lendo os dias
                        for dia in lista_horarios_reais:
                            if int(letra) == dia[0]:
                                dias.append(dia[1])  # Adiciona o dia (Segunda, Terça, etc)
                elif letra.isalpha():  # Letra identificando o turno
                    for turno in lista_turno:
                        if letra == turno[0]:
                            letra_turno = letra

            # Atualizar o dicionário de horários para os dias encontrados
            for dia in dias:
                if dia not in dicionario_horarios:
                    dicionario_horarios[dia] = []
                dicionario_horarios[dia].extend(horarios)

            # Acumular os resultados deste bloco nos resultados gerais
            printar_main_geral.extend(printar_main)

        # Retornar os resultados acumulados
        resultado_geral = [dicionario_horarios, printar_main_geral]
        print(resultado_geral)
        return resultado_geral

    def exibir_grade(self, lista_recebida):
        # Define dias e horários fixos
        dias = ["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        horarios = [
            "08:00 - 09:00", "09:00 - 09:50", "10:00 - 11:00", "11:00 - 11:50",
            "12:00 - 13:00", "13:00 - 13:50", "14:00 - 15:00", "15:00 - 15:50",
            "16:00 - 17:00", "17:00 - 17:50", "18:00 - 19:00", "19:00 - 19:50",
            "19:50 - 20:40", "20:50 - 21:40", "21:40 - 22:30"
        ]

        # Estrutura para armazenar a grade consolidada
        grade = {dia: {horario: [] for horario in horarios} for dia in dias[1:]}  # Ignora "Hora"
        print(lista_recebida)
        # Preencher a grade com as matérias
        for lista in lista_recebida:
            
            if len(lista[0][0]) > 10:
                palavras = lista[0][0].split()
                materia = lista[0][1]
                print(materia)         
            else:
                materia = lista[0][0]
            turno_dias = lista[1]
            turnos = lista[2]

            for idx, horario in enumerate(horarios):
                turno_atual = ""
                if idx < 5: #idx é igual a um numero sequencial ex:(123), dado a cada horario
                    turno_atual = f"M{idx + 1}"
                elif 5 <= idx < 10:
                    turno_atual = f"T{idx - 4}"
                elif idx >= 10:
                    turno_atual = f"N{idx - 9}"

                if turno_atual in turnos:
                    for dia in turno_dias:
                        grade[dia][horario].append(materia)


        print("     Hora     |    Segunda   |     Terça    |    Quarta    |    Quinta    |    Sexta     |    Sábado    |")

        print("-" * (15 * len(dias)))

        for horario in horarios:
            linha = f"{horario:^12} |"
            for dia in dias[1:]:
                if grade[dia][horario]:
                    materias = ", ".join(grade[dia][horario])
                    linha += f" {materias:^12} |"
                else:
                    linha += f" {'':^12} |"
            print(linha)
            print("-" * (15 * len(dias)))

    def printar_na_main_turma(self,nome_materia, professor, dia, hora, local, horario_unb):
        # Formatação dos dias
        rodar = Grade()
        
        ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        dias = list(dia.keys())
       
        # Código para formatar os dias
        if len(dias) == 1:
            dias_formatados = dias[0]
        elif len(dias) == 2:
            # Ordenar os dias conforme a ordem definida
            dias.sort(key=lambda dia: ordem_dias.index(dia))
            dias_formatados = f"{dias[0]} e {dias[1]}"
        else:
            # Ordenar os dias conforme a ordem definida
            dias.sort(key=lambda dia: ordem_dias.index(dia))
            dias_formatados = ", ".join(dias[:-1]) + f" e {dias[-1]}"
        horarios_formatados = ', '.join(hora)
        

        print(rodar.color_text(
            f"A turma da matéria {nome_materia} que você escolheu é do(a) professor(a) {professor}, "
            f"tem o horário {horario_unb},\nque se aplica no(s) dia(s) {dias_formatados}, "
            f"no horário(s) {horarios_formatados} e na(s) salas {local}.", 
        "magenta"))

    def color_text(self, text, cor, background_color=None, style=0):
        cores = [
            ["preto", 30],
            ["vermelho", 31],
            ["verde", 32],
            ["amarelo", 33],
            ["azul", 34],
            ["magenta", 35],
            ["ciano", 36],
            ["branco", 37]
        ]
        for corzinha in cores:
            if cor == corzinha[0]:
                cor = corzinha[1]
            else:
                pass
        if background_color:
            return f"\033[{style};{cor};{background_color}m{text}\033[0m"
        return f"\033[{style};{cor}m{text}\033[0m"
                    
                #    Normal	0,    Negrito	1,Subtle	2,Sublinhado	4,Piscando	5
                #Cor do Texto ou Fundo	Código
                #Preto	30,Vermelho	31,Verde	32,Amarelo	33,Azul	34,Magenta	35,Ciano	36,Branco	37

    
rodar = Grade()

# rodar.exibir_grade(lista2)
rodar.leitor("35M34 2T45")


##modificar leitor de grade, armazenar dentro de cada hora um varialvel que simbolize o dia.
#fazer com dicionarios a lista horario

