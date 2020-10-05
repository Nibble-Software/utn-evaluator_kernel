import subprocess
import os

cpp_file = 'HolaMundo.cpp'

os.system('g++ ' + cpp_file)

data = subprocess.Popen('a.exe', stdout=subprocess.PIPE).communicate()[0]

resultado = data.decode('utf-8')

print(resultado)

if resultado == "¡HOLA MUNDO!":
    print("Test Passed")
else:
    print("Test Failed")
