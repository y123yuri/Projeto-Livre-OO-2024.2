import sys
import os

#  a pasta "classes" ao caminho de busca de módulos
diretorio_classes = os.path.join(os.path.dirname(__file__), 'classes')
sys.path.append(diretorio_classes)

from arquivo_main import *

main = Main()
main.main()


#botar nome do professor