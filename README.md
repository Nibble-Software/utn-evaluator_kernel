# Nibble-Evaluator
Esto es Nibble Evaluator, una app desarrollada para evaluar código desarrollado por los estudiantes de acuerdo a un conjunto de entradas establecidas y salidas esperadas

# Status del Proyecto

### Anuncios Versión 0.5


- La app puede compilar y ejecutar en C++
- La app puede leer archivos de entrada y salida en formato txt
- La app puede leer multiples salidas obtenidas del ejecutable de C++
- La app puede ingresar entradas en el ejecutable de C++ generado
- Se pueden ejecutar pruebas sobre código cpp que no tenga que recibir valores de entradas
- El sistema puede aceptar entradas y salidas en cualquier orden (Revisar con mas ejemplos)
- Ya esta disponible la CLI para usar el módulo
- La app puede detectar errores de compilación y ejecución,
  devolviendo un status cuando ocurre alguno de los dos errores
- La app ahora ejecuta scripts de python


# Uso del CLI
El CLI recibe tres parámetros:
- La ruta del archivo .cpp a ser ejecutada
- La ruta del archivo txt de entradas
- La ruta del archivo txt de salidas esperadas

Las rutas deben ser escritas de forma Absoluta

Ejemplo de uso
```sh
#Ubicados en la ruta de nibble Evaluator
python main.py "C:\Users\Alpha\Ejemplo.cpp" "C:\Users\Alpha\Inputs.cpp C:\Users\Alpha\Outputs.cpp"
```


# Requisitos de los archivos de entrada y salida

## Formato del archivo de output esperados
- El archivo debe estar en formato .txt
- El archivo debe indicar textualmente la cadena con la salida esperada
- Los saltos de lineas se representan haciendo un salto de linea en el txt

### Ejemplo
Si quiero recibir los numeros del 1 al 5 de forma secuencial se debe mostrar así

```
1 2 3 4 5
```

En cambio si deseo recibirlos linea por linea se debe mostrar así

```
1
2
3
4
5
```


# Desarrollado por
- Marcelo de Jesús Núñez - @chelo154
- José Agustín Sánchez -
- Germán Navarro Alascio
- Iván Arturo Taddei

# Requerimientos

## Software necesario

- MinGW para Windows (Este compilador es exclusivo de Windows, la razón de su uso es que la cátedra de AED usa este compilador. Se puede usar g++ también si se desea)
