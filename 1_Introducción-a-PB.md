# Introducción al curso de PB

A continuación se revisará:

-   ¿Qué se entiende por computadora?

-   ¿Cuáles son las partes de un ordenador?

-   ¿Qué es el software?

-   ¿Qué son los lenguajes de programación y cómo usarlos para programar?

### ¿Qué se entiende por computadora?

Una computadora es una máquina electrónica diseñada para recibir, procesar y almacenar datos, ejecutando una serie de instrucciones conocidas como programas. A través de sus componentes físicos, como el procesador, la memoria y el almacenamiento, y sus componentes lógicos, como el sistema operativo y las aplicaciones, una computadora puede realizar desde cálculos matemáticos simples hasta operaciones complejas, facilitando tareas en casi todos los aspectos de la vida moderna. Es el cerebro detrás de muchas de las tecnologías que utilizamos a diario, capaz de seguir las instrucciones del programador para llevar a cabo una amplia gama de funciones.

### ¿Cuáles son las partes de un ordenador?

#### Tangibles **(Hardware)**:

-   **Unidad Central de Procesamiento (CPU)**: Conocido como el cerebro del ordenador, es responsable de realizar todas las operaciones y cálculos. Procesa las instrucciones que recibe del software.
    
-   **Memoria RAM (Memoria de Acceso Aleatorio)**: Es la memoria a corto plazo de la computadora, donde se almacenan temporalmente los datos y programas que están en uso. Es crucial para el rendimiento, ya que permite que el sistema acceda rápidamente a la información.
    
-   **Placa Base (Motherboard)**: Es la tarjeta principal que conecta todos los componentes del ordenador, como el CPU, la RAM, y otros dispositivos internos y externos.
    
-   **Disco Duro (HDD) o Unidad de Estado Sólido (SSD)**: Son los dispositivos de almacenamiento de largo plazo. Aquí se guardan el sistema operativo, programas, archivos y datos del usuario.
    
-   **Fuente de Alimentación**: Proporciona la energía eléctrica necesaria para que todos los componentes funcionen.
    
-   **Tarjeta Gráfica (GPU)**: Se encarga de procesar y renderizar imágenes y videos. En los ordenadores para juegos o edición de video, la tarjeta gráfica es especialmente importante.
    
-   **Unidad de Disco Óptico**: Aunque cada vez menos común, algunas computadoras tienen unidades para leer y escribir CDs, DVDs o Blu-rays.

-   **Periféricos**: Estos incluyen el teclado, el ratón, la pantalla (monitor), impresoras, altavoces, y cualquier otro dispositivo externo que se conecte a la computadora.

#### Intangibles **(Software)**:

-   **Sistema Operativo (SO)**: Es el software principal que gestiona todos los recursos del ordenador y permite la interacción entre el usuario y el hardware. Ejemplos incluyen Windows, macOS, GNU/Linux, TempleOS y más.
    
-   **Aplicaciones y Programas**: Son los programas que instalas para realizar tareas específicas, como navegadores web, procesadores de texto, editores de imágenes, juegos, etc.
    
-   **Firmware**: Es un tipo de software específico que está integrado en el hardware y proporciona control básico sobre los dispositivos.

### ¿Qué son los lenguajes de programación y cómo usarlos para programar?

Los lenguajes de programación son sistemas formales compuestos por un conjunto de reglas y sintaxis que permiten a los programadores escribir instrucciones para que una computadora realice tareas específicas. Piensa en ellos como un medio de comunicación entre humanos y máquinas. Así como el español o el inglés permiten a las personas entenderse, los lenguajes de programación permiten que un programador "hable" con una computadora para indicarle qué hacer.

Existen muchos lenguajes de programación, cada uno diseñado con un propósito específico o con características que lo hacen más adecuado para ciertos tipos de tareas. Por ejemplo, **Python** es conocido por su simplicidad y versatilidad, lo que lo convierte en un buen lenguaje para principiantes y para desarrollo web, análisis de datos, y automatización. **JavaScript** es fundamental para el desarrollo de aplicaciones web interactivas, mientras que **C++** y **Java** son populares en el desarrollo de software de alto rendimiento y aplicaciones móviles.

Tradicionalmente, en un curso universitario de programación, se haría una breve introducción a la sintaxis de un lenguaje de programación como C o C++ para inmediatamente después pasar a DSA (Data Structures and Algorithms) y continuar aprendiendo y dominando los fundamentos sobre la marcha. Sin embargo, la UDEP tomó la decisión de desarrollar los aspectos más básicos de la programación y la sintaxis de Python durante un ciclo entero, lo que representa una oportunidad para subir nota.

Regresando a la teoría, los lenguajes de programación se pueden dividir en tres grupos por tipo de ejecución:

- **Compilados**: Los lenguajes de programación compilados son aquellos que se traducen directamente a código máquina antes de su ejecución. Esto significa que el compilador analiza el código fuente y genera un archivo ejecutable que puede ser ejecutado directamente por la máquina sin necesidad de interpretación adicional.

- **Interpretados**: Los lenguajes de programación interpretados son aquellos que se traducen línea por línea en tiempo real, a medida que se ejecuta el programa. En otras palabras, el intérprete ejecuta el código fuente directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina.

- **Interpretados y compilados (Virtuales)**: Los lenguajes de programación virtuales son aquellos que se ejecutan en una máquina virtual (VM), que es un entorno de ejecución independiente del sistema operativo y hardware físico. Estos lenguajes se compilan en bytecode, que es interpretado por la máquina virtual, en lugar de ser traducidos directamente a código máquina.

#### Paradigmas de programación

Otra diferenciación básica entre lenguajes de programación es o puede ser su paradigma. Los paradigmas de programación son estilos o modelos para resolver problemas computacionales.

Los tres paradigmas de lenguajes de programación más populares son:

-	**Imperativo o procedimental**: El programador debe definir explícitamente el orden en que se ejecutan las instrucciones y cómo se toman decisiones. Además, las variables y estructuras de datos se modifican a lo largo de la ejecución del programa, reflejando el progreso hacia la solución del problema.

-	**Funcional**: El código se enfoca en describir qué se quiere lograr, sin preocuparse por cómo se logra. Las funciones deben ser idempotentes y no tener efectos secundarios, y los datos son inmutables. Además, la programación funcional se basa en la recursividad para resolver problemas, lo que puede ser más eficiente que el enfoque imperativo.
	
-	**Orientado a Objetos (OOP)**: El código en torno a "objetos", que son instancias de "clases". Las clases definen atributos (propiedades) y métodos (funciones) que los objetos pueden tener. 
    
    **Características clave del OOP**

    -   **Encapsulamiento**: la información o estado de los atributos se protege para que no se pueda ver o modificar sin el mecanismo adecuado.
    
    -   **Abstracción**: los objetos representan abstracciones de hechos o entes del mundo real, con atributos que representan características o propiedades y métodos que emulan su comportamiento o actividad.
     
    -   **Herencia**: las clases pueden heredar características y comportamientos de otras clases, permitiendo la creación de una jerarquía de clases y objetos.

Los lenguajes de programación pueden tener un único paradigma o ser multiparadigmas.

**Ejemplos de lenguajes de programación por paradigmas**:

-   Imperativo: C (y soporta funcional)

-   Funcional puro: Haskell, Elm

-   OOP: Java (y soporta funcional)

-   Multiparadigma: C++ y Python (soportan código imperativo, funcional y orientado a objetos)

Realmente, a excepción de algunos lenguajes de programación puramente funcionales, la mayoría de los lenguajes de programación usados actualmente son multiparadigma, manejando código imperativo y funcional.