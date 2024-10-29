# Todos los enunciados de PB 2024-II

## Índice: 

- **Entrada y salida: clase 1**

- **Condicionales if elif else: clases 2, 3 y 4**

- **Bucles while y for: clases 5, 6, 7 y 8**

- **Fechas: clases 9,10 y 11**

- **Arrays: clases 12 y 13**

## Clase 1

1.  Escriba un programa que pida el año de nacimiento e imprima la edad.

2.  Escriba un programa que pida el nombre y la edad e imprima un mensaje con la edad.

## Clase 2

1. Haga un programa que lea si se sacó 20 e imprima "Excelente".

2. Escriba un programa que lea el año de nacimiento y calcule la edad e imprima si es mayor o menor de edad.

3. Escriba un programa que lea el año de nacimiento y calcule la edad e imprima su grupo etario: 0 -17: primera, 18 - 60: segunda, 61 - 100: tercera.

4. Haga un programa que indique el horario de presentación en olimpiadas:
Los programas académicos: IIS, ADS, PSI, DER : 11am
Los programas académicos: ADE, MED, ECO, HYG : 12pm
El programa debe de preguntar en que programa académico se encuentra e imprimir en qué horario le corresponde presentarse.

## Clase 3

1. ### Caso: Programa de Vacunación

Se está vacunando a personas mayores de 30 años. Escriba un programa que:

1. Pregunte al usuario su edad.
2. Pregunte si viene por su primera o segunda dosis.

#### Reglas:

- Si viene por su **primera dosis**, le corresponde **Sinopharm**.
- Si viene por su **segunda dosis**, el programa debe preguntar qué vacuna se le aplicó en la primera dosis y se le debe aplicar la **misma vacuna**.

#### Vacunas válidas:

- Pfizer
- Sinopharm

#### El programa debe imprimir:

- Si le corresponde vacunarse.
- Qué dosis le toca.
- Qué vacuna le corresponde.

2. ### Caso: Validación de inscripción a cursos

Se desea hacer un programa que valide la inscripción de un alumno en un curso. Para que el alumno se pueda inscribir debe cumplir las siguientes condiciones:

   a. Haber aprobado el requisito o haberlo desaprobado con 10  
   b. Estar al menos en ciclo requisito  
   c. Tener al menos los créditos requisito aprobados  
   d. No tener cruce de horas, o en su defecto, tener un cruce menor al 50% de las horas semanales (1 crédito = 1 hora semanal).

Haga un programa que solicite al alumno los siguientes datos: (8p)

- Curso al que desea matricularse  
- Ciclo en el que está el alumno  
- Créditos aprobados del alumno  
- Si ya llevó el requisito o no  
  - En caso de que sí lo haya llevado: promedio con que dejó el curso requisito  
- Si hay cruce de horas o no  
  - En caso de que haya cruce: cantidad de horas de cruce  

El programa debe imprimir si se puede inscribir en el curso o no. (12p)

A continuación, se muestran los cursos y sus requisitos. Si el curso que desea llevar no aparece en la tabla, el programa debe indicar que sí puede llevarlo.

## Clase 4

### Programa para definir las modalidades de admisión

Se desea hacer un programa para definir las modalidades de admisión que existen para un postulante a la Universidad. El postulante debe registrarse con los siguientes datos:
- Nombres
- Apellidos
- Edad
- Año en que terminó el colegio
- Si su colegio está certificado
- Si fue quinto superior

Todos estos datos deben ser solicitados por el programa.

#### Requisitos y modalidades de admisión:

- Para **4to de secundaria o menor**, la modalidad es: **Simulación de examen de admisión**.
- Para **5to de secundaria o alumnos que ya terminaron el colegio**, las modalidades dependen de los siguientes factores:

| Edad               | Requisitos                         | Año de término | Colegio certificado | Quinto superior | Modalidad                 |
|--------------------|------------------------------------|----------------|---------------------|-----------------|---------------------------|
| 18 años o mayor     | Antecedentes penales, Libretas de secundaria | N/A            | N/A                 | N/A             | Examen de admisión         |
| Menor de 18 años    | Libretas de secundaria             | 2021           | N/A                 | N/A             | Examen de admisión         |
| Menor de 18 años    | Libretas de secundaria             | 2022           | No                  | N/A             | Examen de admisión         |
| Menor de 18 años    | Libretas de secundaria             | 2022           | Sí                  | No              | Examen de admisión         |
| Menor de 18 años    | Libretas de secundaria             | 2022           | Sí                  | Sí              | Ingreso directo            |
| Menor de 18 años    | Libretas de secundaria             | 2023           | No                  | N/A             | Examen de admisión         |
| Menor de 18 años    | Libretas de secundaria             | 2023           | Sí                  | Sí              | Ingreso directo            |
| Menor de 18 años    | Libretas de secundaria             | 2023           | Sí                  | No              | Entrevista de admisión     |

N/A significa que no se aplica ese criterio para la modalidad de admisión.

## Clase 5

1. Escriba un programa que lea un número entero y valide que sea positivo y par

2. Escriba un programa que solicite al usuario ingresar 6 números e imprima el menor

## Clase 6

1. Escriba un programa que lea 6 notas y las valide. El programa debe calcular el promedio anulando la nota menor.

2. Escriba un programa que lea un número de al menos 2 digitos e imprima cuantos digitos tiene.

## Clase 7

1. Escriba un programa que lea un número entero no negativo e imprima el valor de su factorial.

2. Escriba un programa que lea 3 números a, b, c e imprima los valores generados por range (a, b, c).

3. Haga un programa que lea un número entero positivo e imprima si es primo.

## Clase 8

1. Haga un programa que lea 2 números e imprima si son números amigos.
- Amigos: la suma de los divisores propios de uno es igual al otro y viceversa.
- Los números deben de ser naturales.

2. Escriba un programa que lea un número natural e imprima si es capicúa. Para ser capicúa debe cumplir lo siguiente: debe leerse igual de derecha a izquierda que de izquierda a derecha; el número debe ser de al menos 2 digitos.

3. Escriba un programa que lea un número entero positivo e imprima si es un número narcisista.
- Numeroso narcisista: la suma de sus digitos elevados a la cantidad de sus digitos es igual al mismo número.
- Debe de tener al menos 2 digitos.

## Clase 9

1. Escribe un programa que lea una fecha y la valide.

2. Escriba un programa que lea 2 fechas y las valide. El programa debe imprimir cual es la fecha mayor.

## Clase 10

1. Escriba un programa que lea 2 fechas y valide que la segunda fecha es mayor que la primera. 

2. Escriba un programa que lea una fecha y calcule el dia del año.

3. Escriba un programa que lea 1 fecha y calcule cuántos días faltan para que acabe el año.

## Clase 11

1. Escribir un programa que lea 2 fechas del mismo año y calcule cuántos días hay entre las 2.

2. Escribi un programa que lea 2 fechas de años distintos (la 2da fecha es mayor que la 1ra), y calcule cuántos días hay entre las 2 fechas.

## Clase 12

1. Escriba un programa que pida los nombres de 5 amigos y los guarde en una lista.

2. Escriba un programa que lea y valide 6 notas. Las notas se deben guardar en una lista e imprimir el promedio. El promedio se debe calcular a partir de la lista. 

3. Escriba un programa que lea y valide 6 notas. Las notas se deben guardar en una lista e imprimir el promedio ponderado. Las notas y los pesos se deben guardar en 2 listas.

4. Escriba un programa que lea y valide 6 notas. Las notas se deben guardar en una lista e imprimir el promedio sin contar la nota mínima. 

## Clase 13

1. Escriba un programa que lea 1 fecha y la valide.

2. Escribir un programa que lea 2 fechas y calcule la diferencia de días entre ellas.

## Clase 14

1. Escriba un programa que pida al usuario un número e imprima si está o no está en la lista.

2. Escriba un programa que lea un número y valide que esté en la lista.

3. Dada la lista x, haga un programa que guarde las frecuencias de todos sus valores en una lista f. 

## Clase 15

1. Imprimir cuantas veces aparece cada valor de x sin repetir ninguno de los valores.

2. Dada la lista x, haga un programa que imprima qué valor se repite más.

3. Dada la lista x, haga un programa que imprima los valores más frecuentes de x y cuántas veces se repite cada uno.

4. Dada la lista, escriba un programa que calcule el promedio anulando los dos valores más bajos.

## Clase 16

1. Dada una lista X, haga un programa que encuentre los 2 menores valores de la lista.

2. Dada la lista, ordenar los valores en forma ascendente.

3. Escriba un programa que lea 10 notas de prácticas y calcule el promedio anulando las tres menores.