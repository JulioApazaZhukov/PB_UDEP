/*  
*   Este código incluye una serie de algoritmos básicos en forma de funciones que podrán ser seleccionadas y probadas desde la terminal.
*   Código no optimizado.
*   La terminal no soporta tildes (en las variables y funciones)
*/

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

//  Comprueba si un número es primo
void esPrimo(void){
    int numero, prueba;
    bool comprobacion = 1;
    cout << "Ingrese un numero entero positivo: ";
    do {
        cin >> numero;
    } while(numero <= 0);
    prueba = numero-1;
    while(prueba > 1){
        if (numero % prueba == 0){comprobacion = 0;}
        prueba--;
    }
    if (comprobacion == 1){cout << "Es Primo";} else {cout << "No es primo";}
}

//  Calcula el factorial de un número
void factorial(void){
    int numero, productoFactorial = 1;
    cout << "Ingrese un numero entero positivo: ";
    do {
        cin >> numero;
    } while(numero < 0);
    if (numero == 0){
        cout << "El producto factorial es 1";
    } else{
        while(numero > 0){
        productoFactorial *= numero;
        numero--;
        }
        cout << "El producto factorial es " << productoFactorial;
    }
}

//  Escribe la sucesión Fibonacci
void secuenciaDeFibonacci(void){
    int numero, auxiliar1, auxiliar2, rango;
    cout << "Ingrese un numero entero positivo: ";
    do {
        cin >> rango;
    } while(rango < 0);
    numero = 0;
    auxiliar1 = 0;
    auxiliar2 = 1;
    cout << numero + auxiliar2 << " ";
    while(rango > 1){
        numero = auxiliar1 + auxiliar2;
        auxiliar1 = auxiliar2;
        auxiliar2 = numero;
        cout << numero << " ";
        rango--;
    }
}

//  Calcula el promedio ponderado
void promedioPonderado(void){
    int nota, notaProducto, peso, pesoSuma;
    notaProducto = pesoSuma = 0;
    char continuar;
    do {
        cout << "Ingrese nota: ";
        cin >> nota;
        cout << "Ingrese peso: ";
        cin >> peso;
        cout << "Continuar ingresando? (s/n): ";
        cin >> continuar;
        notaProducto += nota*peso;
        pesoSuma += peso;
    } while(continuar == 's');
    float promedio = notaProducto / pesoSuma;
    cout << "El promedio ponderado es: " << promedio << endl;
}

//  Parte de la función bubblesort
void printArray(int array[], int size){
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

//  Parte de la función bubblesort
void swap(int array[], int i){
    int aux = array[i];
    array[i] = array[i+1];
    array[i+1] = aux;
}

//  Aplica bubblesort a una serie de números ingresados por el usuario
void bubbleSort(void){
    int array[100];
    char continuar;
    int i = 0;
    do {
        cout << "Ingrese un elemento: ";
        cin >> array[i];
        cout << "Ordenar?(s) ";
        cin >> continuar;
        i++;
    } while(continuar != 's');
    cout << endl;
    int size = i;
    printArray(array, size);
    for (int j = 0; j < size; j++){
        int aux = 0;
        for (int i = 0; i < size; i++){
            if (array[i] > array[i+1]){
                swap(array, i);
            }
        }
    }
    printArray(array, size);
}

void imprimirNumerosPrimos(void){
    int numero, prueba;
    numero = 3;

    while(true){
        bool comprobacion = 1;
        prueba = numero - 1;
        while(prueba > 1){
            if (numero % prueba == 0){comprobacion = prueba = 0;}
            prueba--;
        }
        if (comprobacion == 1){cout << numero << endl;} 
        numero = numero + 2;
    }
}

int main(void){
    int input;
    char continuar;
    do{
        cout << "Elija una opcion: " << endl << "1. Comprueba si un numero es primo" << endl << "2. Calcula el factorial de un numero" << endl << "3. Escribe la sucesion de Fibonacci" << endl << "4. Calcula el promedio ponderado" << endl << "5. Ordena numeros (Bubblesort)" << endl << "6. Imprimir todos los numeros primos que int es capaz de representar" << endl;
        cin >> input;
        switch (input){
        case 1:
            esPrimo();
            break;
        case 2:
            factorial();
            break;
        case 3:
            secuenciaDeFibonacci();
            break;
        case 4:
            promedioPonderado();
            break;
        case 5:
            bubbleSort();
            break;
        case 6:
            imprimirNumerosPrimos();
            break;
        default:
            break;
        }
        cout << endl << "Continuar? (s/n)" << endl;
        cin >> continuar;
    } while(continuar == 's');

    return 0;
}