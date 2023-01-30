#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main ()
{
	int a ,b , c ;
	
	cout << "INGRESE LA BASE MAYOR  " <<endl;
	cin >> a ;
	cout << "INGRESE LA BASE MENOR  " <<endl;
	cin >> b ;
	cout << "INGRESE LA ALTURA " << endl ;
	cin >> c ;
	
	//system ("cls") ;
	
	int dat1=a+b ;
	int dat2=dat1*c ;
	int dat3=dat2/2 ;
	
	cout << "EL AREA DEL TRAPECIO ES :" << dat3 << endl ;
}