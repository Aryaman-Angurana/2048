#include <iostream>
#include <conio.h>

using namespace std;

int table[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
char command = ' ';

void draw()
{
    system("cls");
    cout << "\t\t\t\t\t\t\t\t    2048\n\n";
    cout << "\t\t\t\t\t\t\t-----------------------------" << endl;
    for (int i = 0; i < 4; i++)
    {
        cout << "\t\t\t\t\t\t\t|";
        for (int j = 0; j < 4; j++)
        {
            if (table[i][j] == 0)
                cout << "      |";
            else if (table[i][j] / 10 < 1)
                cout << "    " << table[i][j] << " |";
            else if (table[i][j] / 100 < 1)
                cout << "   " << table[i][j] << " |";
            else if (table[i][j] / 1000 < 1)
                cout << "  " << table[i][j] << " |";
            else if (table[i][j] / 10000 < 1)
                cout << " " << table[i][j] << " |";
        }
        cout << endl;
        cout << "\t\t\t\t\t\t\t-----------------------------" << endl;
    }
}


void input()
{
    cout << "Commands: \nPress the arrow keys for commands: ";
    // -32, 77 --> LEFT KEY
    // -32, 75 --> RIGHT KEY
    // -32, 72 --> UP KEY
    // -32, 80 --> DOWN KEY
    char x = _getch();
    char y = _getch();
}


void logic()
{

}


int main()
{
    draw();
    input();
    return 0;
}














