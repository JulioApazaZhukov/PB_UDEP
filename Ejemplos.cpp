/*  
*   Este código incluye una serie de algoritmos básicos en forma de funciones que podrán ser seleccionadas y probadas desde la terminal.
*   Los algoritmos a continuación son sencillos, pero no necesariamente son óptimos para la resolución del respectivo problema.
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
    do{
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
    do{
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
    do{
        cin >> rango;
    } while(rango < 0);
    numero = 0;
    auxiliar1 = 0;
    auxiliar2 = 1;
    cout << numero + auxiliar2 << " ";
    while (rango > 1){
        numero = auxiliar1 + auxiliar2;
        auxiliar1 = auxiliar2;
        auxiliar2 = numero;
        cout << numero << " ";
        rango--;
    }
}   // Spaguetti

int main(void){
    int input;
    char continuar;
    do{
        cout << "Elija una opcion: " << endl << "1. Comprueba si un numero es primo" << endl << "2. Calcula el factorial de un numero" << endl << "3. Escribe la sucesion de Fibonacci" << endl;
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
        default:
            break;
        }
        cout << endl << "Continuar? (s/n)" << endl;
        cin >> continuar;
    } while(continuar == 's');

    int finalizar;
    cin >> finalizar;
    return 0;
}