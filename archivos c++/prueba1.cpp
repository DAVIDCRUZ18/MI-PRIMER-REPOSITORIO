/* Programa: Saludo */

#include <conio.h>
#include <stdio.h>

int main()
{
    char nombre[20];

    printf( "Introduzca su nombre: " );
    scanf( "%s", nombre );
    printf( "Hola %s, buenos dias.", nombre, 161 );

    getch(); /* Pausa */

    return 0;
}