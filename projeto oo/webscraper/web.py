from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
link = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get(link)

try:
    driver.find_element("xpath", "/html/body/dialog/button").click()  # cookie ciente
except:
    pass

unidade_elemento = driver.find_element("xpath", '//*[@id="formTurma:inputDepto"]')
unidade_select = Select(unidade_elemento)
turmas_lista = []
professores = []
materias = []
print(unidade_select)

for op in range(1, len(unidade_select.options)):
    start_time = time.time()
    unidade_elemento = driver.find_element("xpath", '//*[@id="formTurma:inputDepto"]')
    unidade_select = Select(unidade_elemento)
    unidade_select.select_by_index(op)
    busca = driver.find_element("xpath", '/html/body/div/div/div[2]/form/table/tfoot/tr/td/input[1]')
    busca.click()

    try:
        tabela = driver.find_element("xpath", '/html/body/div/div/div[2]/form/div[2]/table')
    except:
        tabela = False

    if tabela:
        rows = tabela.find_elements("tag name", "tr")
        materia = ''
        
        for linha in rows[1:-1]:
            if linha.get_attribute("class") == "agrupador":  # MATÉRIA
                print("--" * 25)
                print(linha.text)
                materia = linha.text.split(" ")[0]
                materias.append([materia, linha.text[linha.text.index("-") + 1:]])
                professores = []  # Reinicia a lista para nova matéria
            
            else:  # TURMA
                info = linha.find_elements('tag name', 'td')  # n°turma/periodo/nome_prof/horario/quantvagas/quantvagasOcupadas/local
                horarios = info[3].text.strip()  # Pega o horário da turma
                
                if '(' in info[2].text:
                    texto_completo = info[2].text
                    info[2] = info[2].text[:info[2].text.index('(') - 1]
                    index = texto_completo.index(')') + 2
                    while len(texto_completo) > index:
                        texto_completo = texto_completo[index:]
                        print(texto_completo[:texto_completo.index('(') - 1])
                        info[2] += ";" + texto_completo[:texto_completo.index('(') - 1]
                        index = texto_completo.index(')') + 2
                        print(index, len(texto_completo))
                else:
                    info[2] = info[2].text
                
                # Permitir turmas com mesmo professor e matéria, mas horários diferentes
                turma = {
                    "materia": materia,
                    "professor": info[2],
                    "turno": horarios,
                    "local": info[7].text
                }
                if turma not in turmas_lista:  # Verifica duplicação de forma completa
                    turmas_lista.append(turma.copy())
                    print(turma)
        
        print('-=-=-=-=-=' * 15)
        unidade_elemento = driver.find_element("xpath", '//*[@id="formTurma:inputDepto"]')
        unidade_select = Select(unidade_elemento)
        print(unidade_select.options[op].text)
        print("--- %s seconds ---" % (time.time() - start_time))

with open("turmas.txt", 'w') as fp:
    for t in turmas_lista:
        fp.write('$'.join(list(t.values())))
        fp.write('\n')

with open("materias.txt", "w") as fp:
    for m in materias:
        fp.write("$".join(m))
        fp.write('\n')
