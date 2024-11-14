# Função para exibir uma grade horária no terminal
import time

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
    

printar()
