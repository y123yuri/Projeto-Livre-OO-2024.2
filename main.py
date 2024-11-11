import sys
import os

# 2
#  a pasta "classes" ao caminho de busca de módulos
diretorio_classes = os.path.join(os.path.dirname(__file__), 'projeto oo\classes')
sys.path.append(diretorio_classes)

# Agora você pode importar as classes
from buscar import *
from executor_txt import *
from shapes import *
from arquivo_main import *

main = Main()
main.main()
