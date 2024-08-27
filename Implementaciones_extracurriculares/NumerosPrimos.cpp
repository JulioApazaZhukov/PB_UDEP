//  Algoritmo optimizado para hallar números primos en C++
#include <iostream>

using std::cout;
using std::endl;

int main(void){
    int numero, prueba;
    float limite;
    numero = 3;
    cout << "1" << endl << "2" << endl;
    while(true){
        bool comprobacion = 1;
        prueba = 3;
        limite = (numero / 3) + 1;
        while(prueba < limite && comprobacion == 1){
            if (numero % prueba == 0){comprobacion = 0;}
            prueba++;
        }
        if (comprobacion == 1){cout << numero << endl;}
        numero = numero + 2;
    }

    return 0;
}