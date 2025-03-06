#include <iostream>
#include <windows.h>
#include <chrono>

using std::cout;
const char solid = char(254);

void gotoxy (int x, int y)
{
    COORD coordinate;
    coordinate.X = x;
    coordinate.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coordinate);
}

void border ()
{
    for(int i = 1; i < 27; i++){
        gotoxy(1,i); cout << char(186);
        gotoxy(99,i); cout << char(186);
    }
    for(int i = 2; i < 99; i++){
        gotoxy(i,0); cout << char(205);
        gotoxy(i,27); cout << char(205);
    }
    gotoxy(1,0);    cout << char(201);
    gotoxy(1,27);   cout << char(200);
    gotoxy(99,0);   cout << char(187);
    gotoxy(99,27);  cout << char(188);
}

void loading ()
{
    int turn = 0;
    while (true)
    {
        int a;
        if (turn == 0)
        {
            for (int i = 5; i < 85; i++){
                Sleep(10);
                gotoxy(i,5); cout << solid;
                a = i;
            }
            if (a == 84){
                turn = 1;
            }
        } else if (turn == 1)
        {
            for (int i = 5; i < 11; i++){
                Sleep(10);
                gotoxy(84,i); cout << solid;
                a = i;
            }
            if (a == 10){
                turn = 2;
            }
        } else if (turn == 2)
        {
            for (int i = 84; i > 5; i--){
                Sleep(10);
                gotoxy(i,10); cout << solid;
                a = i;
            }
            if (a == 6){
                turn = 3;
            }
        } else if (turn == 3)
        {
            for (int i = 10; i > 5; i--){
                Sleep(10);
                gotoxy(5, i); cout << solid;
                a = i;
            }
            if (a == 6){
                turn = 0;
            }
        }              
    }
    
    for (int i = 5; i < 85; i++){
        Sleep(10);
        gotoxy(i,15); cout << solid;
    }
}

int main ()
{
    border();
    loading();
    return 0;
}