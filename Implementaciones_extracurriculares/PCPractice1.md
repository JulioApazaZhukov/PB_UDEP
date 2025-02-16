# PC Practice Nº1
### 1. Función `agregar` (1 punto)
Escriba la función `agregar`, que recibe como parámetros un **array** y una **cadena**.  
La función debe retornar el array con la cadena agregada al final.

### 2. Función `insertar` (5 puntos)
Escriba la función `insertar`, que recibe como parámetros un **array**, una **cadena** y una **posición**.  
La función debe retornar el array con la cadena insertada en la posición indicada, sin perder ninguno de los valores del array original.

### 3. Función `buscar` (2 puntos)
Escriba la función `buscar`, que recibe como parámetros un **array** y una **cadena**.  
La función debe retornar la posición donde se encuentra la cadena en el array.  
Si no la encuentra, debe retornar `-1`.

## 4. Programa con Menú (2 puntos)
Escriba un programa que cree un array `x` e imprima el siguiente menú:
a. Agregar 
b. Insertar 
c. Buscar 
d. Limpiar

El programa debe solicitar al usuario ingresar una opción (`a`, `b`, `c`, `d`).  
- Si el usuario ingresa una cadena que no es ninguna de las 4 opciones, el programa debe volver a pedir que ingrese una opción.  
- Si el usuario ingresa una cadena vacía como opción, el programa termina.

### 5. Implementación de Funcionalidades (10 puntos)
- Si el usuario elige **`a`**, **`b`** o **`c`**, el programa deberá llamar a la función correspondiente de las preguntas anteriores.  
  Para ello, solicitará los datos necesarios, considerando que el array pasado como parámetro es `x`, y los demás datos se leerán del usuario.
- **Validaciones**:
  - Para la opción `b` (insertar), se debe validar que la posición ingresada exista en el array.
  - Para la opción `c` (buscar), si la cadena se encuentra en el array, se debe imprimir:
    ```
    Se encontró en (posición)
    ```
    Si no se encuentra, imprimir:
    ```
    No se encontró
    ```
- Si el usuario elige **`d`**, el programa debe vaciar el array (`x`).
- Luego de cada operación, el programa debe imprimir el array actualizado y volver a mostrar el menú dentro de un bucle.
- **Todos los datos ingresados por el usuario deben validarse correctamente.**

### 6. Consideraciones Adicionales
Puede agregar otras funciones que considere necesarias para mejorar la implementación.

## [Solución](PCPractice1.py)