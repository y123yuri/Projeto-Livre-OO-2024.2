class Grade():
    def leitor(self,codigo_horario):
        horario = codigo_horario
        resultado = []
        mudar_para_horario = False
        letra_turno = ""
        dias = []
        horarios = []
        for letra in horario:
            try:
                letra = int(letra)
                
                if mudar_para_horario == True:

                    lista_horarios_feitos = [["M1", "08:00 - 09:00"], ["M2", "09:00 - 09:50"], ["M3", "10:00 - 11:00"], ["M4", "11:00 - 11:50"], ["M5", "12:00 - 13:00"], ["T1", "13:00 - 13:50"], ["T2", "14:00 - 15:00"], ["T3", "15:00 - 15:50"], ["T4", "16:00 - 17:00"], ["T5", "17:00 - 17:50"], ["N1", "19:00 - 19:50"], ["N2", "19:50 - 20:40"], ["N3", "20:50 - 21:40"], ["N4", "21:40 - 22:30"]]
                    numero_mais_turno = (f"{letra_turno}{letra}")
                    for horario in lista_horarios_feitos:
                        if horario[0] == numero_mais_turno:
                            horarios.append(horario[0])
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

        resultado = [dias, horarios, [letra_turno]]
        print(resultado)
        return resultado
                        
                
                

    def printar():
        

        # Cabeçalhos
        dias = ["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        horarios = [
            "08:00 - 09:00", "09:00 - 09:50", "10:00 - 11:00", "11:00 - 11:50",
            "12:00 - 13:00", "13:00 - 13:50", "14:00 - 15:00", "15:00 - 15:50",
            "16:00 - 17:00", "17:00 - 17:50", "18:00 - 19:00", "19:00 - 19:50",
            "19:50 - 20:40", "20:50 - 21:40", "21:40 - 22:30"
        ]
        
        # Largura de cada coluna
        linhas = 15
        cabecalho = "".join(dia.center(linhas) for dia in dias)
        
        # Imprime cabeçalho
        print(cabecalho)
        print("=" * (linhas * len(dias)))
        

    
rodar = Grade()



