# Datos, variables y operadores

### Tipos de datos

-	int (Entero)

-	float (Real)

-	double (Float de mayor precisión)

-	string (Cadena)

-	bool (Booleano) 

-	char (Caracteres ASCII)

Breve explicación adicional: En clase el profesor mencionó los tipos de datos "más comunes": int, float y string. Int proviene de "integer", que se traduce como entero; float se traduce como flotante, y se le llama así debido a que soporta punto flotante (decimales), y por último string o cadena, que se refiere a una cadena de caracteres, sean números, letras o símbolos.

Sin embargo, hay más tipos de datos que se pueden considerar básicos y que son importantes de tener en cuenta. Por ejemplo: los datos int y float suelen tener el mismo tamaño, que suele ser 4 bytes. Sin embargo, y debido a su tamaño, los fatos float son eficientes en cuanto a memoria, pero no tan óptimos en cuanto a precisión, por lo que, si lo que necesitas es una variable que pueda almacenar muchos decimales sin perder precisión, double es una mejor opción, ya que por lo general tiene un tamaño de 8 bytes (el doble que un float).

Otros tipos de datos muy importantes son bool, que puede ser verdero o falso, 1 o 0, y char, que almacena un código compatible con el sistema de cualquier tipo (número, letra o símbolo).

### Nombres de variables

A la hora de nombrar una variable hay que tener en cuenta ciertas reglas que pueden variar entre lenguajes de programación. Las reglas más comunes son:

-	Acepta letras, números y sub-guiones

-	Primera letra en minúscula

-	Puede llevar números

-	No puede llevar espacios

#### Operaciones

**Asignación**: Se le asigna un valor a una variable haciendo uso del símbolo "=".

```cpp

int edad = 18;

float altura = 1.80;

std::string nombre = "Julio";	// C++ maneja las cadenas de una forma distinta a Python
								// Las asignaciones a variables string van entre comillas dobles

```

**Operadores matemáticos**: Suma, resta, multiplicación, división y modulo(residuo de división):

```cpp
// + - * / %

int num1 = 10;
int num2 = 5;
int num3 = 7;

int sum = num1 + num2;			// 15
int rsta = num1 - num2;			// 5
int mult = num1 * num2;			// 50
int div = num1 / num2;			// 2
int resid = num1 % (num3);		// 3
```

**Operadores lógicos**: Los operadores lógicos se refieren a los condicionales "y" (conjunción), "o" (disyunción) y "no" (negación).

```cpp
// p y q pueden ser proposiciones o valores (datos)
if(p == q){}		// Si se cumple que p es igual a q
if(p != q){}		// Si se cumple que p es distinto de q
if(p && q){}		// Si se cumple que p y q se cumplen
if(p || q){}		// Si p o q se cumplen
```

### Nota adicional sobre estructuras de datos

Las estructuras de datos son formas organizadas de almacenar y gestionar datos en un sistema informático, de manera que puedan ser utilizados de una manera más eficiente. Las estructuras de datos más simples de comprender (y que probablemente veremos hacia el final del curso de PB) son los arreglos de una y dos dimenciones (matrices).

Otras estructuras de datos de tipo abstracto son: las listas enlazadas, las pilas (stacks), las colas (queues), los árboles (como el árbol binario y el B-Tree), los grafos y las tablas de hash.

***Más sobre las estructuras de datos abstractos más adelante.***

#### Nota
Esta hoja la he escrito completamente a mano, usando como única herramienta adicional un autocorrector algo intrusivo, por lo que agradecería que me avisen si avistan algún error ortográfico o alguna palabra fuera de lugar.