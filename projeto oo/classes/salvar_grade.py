class Grade():
    def leitor(self,codigo_horario):
        horario = codigo_horario
        resultado = []
        mudar_para_horario = False
        letra_turno = ""
        dias = []
        horarios = []
        printar_main = []
        for letra in horario:
            try:
                letra = int(letra)
                
                if mudar_para_horario == True:

                    lista_horarios_feitos = [["M1", "08:00 - 09:00"], ["M2", "09:00 - 09:50"], ["M3", "10:00 - 11:00"], ["M4", "11:00 - 11:50"], ["M5", "12:00 - 13:00"], ["T1", "13:00 - 13:50"], ["T2", "14:00 - 15:00"], ["T3", "15:00 - 15:50"], ["T4", "16:00 - 17:00"], ["T5", "17:00 - 17:50"], ["N1", "19:00 - 19:50"], ["N2", "19:50 - 20:40"], ["N3", "20:50 - 21:40"], ["N4", "21:40 - 22:30"]]
                    numero_mais_turno = (f"{letra_turno}{letra}")
                    for horario in lista_horarios_feitos:
                        if horario[0] == numero_mais_turno:
                            horarios.append(horario[0])
                            printar_main.append(horario[1])
                            print(horario[1])
                        else:
                            pass

                else:
                    lista_horarios_reais = [[2,"Segunda"], [3, "Terça"],[4, "Quarta"],[5, "Quinta"], [6, "Sexta"], [7,"Sábado"]]
                    for dia in lista_horarios_reais:
                        if letra == dia[0]:
                            dias.append(dia[1])
                        else:
                            pass
            except:
                lista_turno = [["M", "Matutino"], ["T", "Vespertino"], ["N", "Noturno"]]
                for turno in lista_turno:
                    if letra == turno[0]:    
                        letra_turno = letra
                        mudar_para_horario = True
                    else:
                        pass
                        
        resultado = [dias, horarios, printar_main ]
        return resultado
                        
                
                

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

        # Preencher a grade com as matérias
        for lista in lista_recebida:
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

        # Exibir a grade consolidada
        print(" | ".join(f"{dia:^13}" for dia in dias))
        print("-" * (14 * len(dias)))

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

    def printar_na_main_turma(self,nome_materia, professor, dias, local, horario_unb):
        # Formatação dos dias
        if len(dias) == 1:
            dias_formatados = dias[0]
        elif len(dias) == 2:
            dias_formatados = f"{dias[0]} e {dias[1]}"
        else:
            dias_formatados = ", ".join(dias[:-1]) + f" e {dias[-1]}"
        
        print(
            f"A turma da matéria {nome_materia} que você escolheu é do(a) professor(a) {professor}, "
            f"tem o horário {horario_unb},\nque se aplica no(s) dia(s) {dias_formatados}, "
            f"e no(s) lugares {local}."
        )

       
