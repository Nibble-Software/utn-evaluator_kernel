# Nibble-Evaluator
Esto es Nibble Evaluator, una app desarrollada para evaluar código desarrollado por los estudiantes de acuerdo a un conjunto de entradas establecidas y salidas esperadas

# Status del Proyecto

### Anuncios Versión 0.1

- La app puede compilar y ejecutar en C++
- La app puede leer archivos de entrada y salida en formato txt
- La app puede leer multiples salidas obtenidas del ejecutable de C++
- La app puede ingresar entradas en el ejecutable de C++ generado
- Se pueden ejecutar pruebas sobre código cpp que no tenga que recibir valores de entradas

### Consideraciones
- El sistema puede recibir programas en C que pidan un conjunto de entradas y luego
muestren las salidas. Esto es, no se puede ingresar datos y mostrar datos de forma desordenada, la razón por la que actualmente esto no es soportado es debido a problemas de abrazo mortal con el subproceso

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
