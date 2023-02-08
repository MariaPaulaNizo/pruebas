#Pruebas para el cambio de rama
variable = 19947198740834
print("Trabajando inspiradamente")

import os
import sys
file_path = os.path.join(os.path.dirname(__file__), '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))
data_dir = file_dir + '/Data/'
