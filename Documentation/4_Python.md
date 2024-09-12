# Introducción a la sintaxis de Python

### 1. Comentarios:

-   **¿Para qué sirven?** Para dejar notas en tu código que la computadora ignorará, como recordatorios o explicaciones.

-   **¿Cómo se escriben?** Con un `#` al principio de la línea.

```python
# Esto es un comentario
```

### 2. Variables:

-   **¿Qué son?** Lugares donde almacenas datos (como cajas con etiquetas).
-   **¿Cómo se declaran?** Simplemente les das un nombre y les asignas un valor.

```python
nombre = "Manuel"
edad = 20 
```
### 3. Tipos de Datos:

-   **Números enteros:** `int`
-   **Números decimales:** `float`
-   **Texto:** `str`
-   **Booleanos:** `bool` (Verdadero o Falso)

```python
numero_entero = 10
numero_decimal = 3.14
texto = "Hola, Mundo"
es_estudiante = True
```

### 4. Operaciones Matemáticas:

-   **Sumar:** `+`
-   **Restar:** `-`
-   **Multiplicar:** `*`
-   **Dividir:** `/`
-   **Módulo (resto de división):** `%`

```python
suma = 5 + 3    # 8
resta = 10 - 4  # 6
multiplicacion = 7 * 2  # 14
division = 9 / 3  # 3.0
modulo = 10 % 3  # 1
```

### 5. Estructuras de Control:

-   **Condicionales:** Toman decisiones basadas en ciertas condiciones.

```python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

-   **Bucles:** Repetir acciones múltiples veces.

```python
for i in range(5):
    print("Este es el número", i)
```

### 6. Funciones:

-   **¿Qué son?** Bloques de código reutilizable que hacen tareas específicas.
-   **¿Cómo se definen?** Usando la palabra clave `def`.

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Manu")  # Salida: Hola Manu
```