import sys
import os
1
# 2
#  a pasta "classes" ao caminho de busca de módulos
diretorio_classes = os.path.join(os.path.dirname(__file__), 'projeto oo\classes')
sys.path.append(diretorio_classes)

from arquivo_main import *

main = Main()
main.main()
