#include <iostream>

using namespace std;

class Nodo {
    public:
        int valor;
        Nodo* izquierda;
        Nodo* derecha;

        Nodo(int val) {
            valor = val;
            izquierda = nullptr;
            derecha = nullptr;
        }
};

class ArbolBinario {
    public:
        Nodo* raiz;

        ArbolBinario() {
            raiz = nullptr;
        }

        Nodo* insertar(Nodo* nodo, int val) {
            if (nodo == nullptr) {
                return new Nodo(val);
            }
            if (val < nodo -> valor) {
                nodo -> izquierda = insertar(nodo -> izquierda, val);
            } else if (val > nodo -> valor) {
                nodo -> derecha = insertar(nodo -> derecha, val);
            }
            return nodo;
        }

        // Recorrido Inorder (izquierda, raíz, derecha)
        void inorder(Nodo* nodo) {
            if (nodo != nullptr) {
                inorder(nodo->izquierda);
                cout << nodo->valor << " ";
                inorder(nodo->derecha);
            }
        }

        // Recorrido Preorder (raíz, izquierda, derecha)
        void preorder(Nodo* nodo) {
            if (nodo != nullptr) {
                cout << nodo->valor << " ";
                preorder(nodo->izquierda);
                preorder(nodo->derecha);
            }
        }

        // Recorrido Postorder (izquierda, derecha, raíz)
        void postorder(Nodo* nodo) {
            if (nodo != nullptr) {
                postorder(nodo->izquierda);
                postorder(nodo->derecha);
                cout << nodo->valor << " ";
            }
        }
};

int main() {
    ArbolBinario arbol;

    arbol.raiz = arbol.insertar(arbol.raiz, 50);
    arbol.insertar(arbol.raiz, 30);
    arbol.insertar(arbol.raiz, 20);
    arbol.insertar(arbol.raiz, 40);
    arbol.insertar(arbol.raiz, 70);
    arbol.insertar(arbol.raiz, 60);
    arbol.insertar(arbol.raiz, 80);

    // Recorridos
    cout << "Recorrido Inorder: ";
    arbol.inorder(arbol.raiz);  // Salida esperada: 20 30 40 50 60 70 80
    cout << endl;

    cout << "Recorrido Preorder: ";
    arbol.preorder(arbol.raiz);  // Salida esperada: 50 30 20 40 70 60 80
    cout << endl;

    cout << "Recorrido Postorder: ";
    arbol.postorder(arbol.raiz);  // Salida esperada: 20 40 30 60 80 70 50
    cout << endl;

    return 0;
}

/*
    Representación grafica del árbol binario:

         50
       /    \
     30      70
    /  \    /  \
   20  40  60  80

*/