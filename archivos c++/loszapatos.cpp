#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int referencia,talla,costo,precio;
	char disponibilidad; 
    string  descripcion;
    int cantidad ;
    
	cout << "INGRESE LA REFERENCIA DEL PRODUCTO" <<endl;
	cin >> referencia ;
	cout << "INGRESE LA TALLA DEL PRODUCTO" <<endl;
	cin >> talla;
	cout << "INGRESE LA DESCRIPCION DEL PRODUCTO" <<endl;
	cin >> descripcion;
	//cout << "INGRESE LA DESCRIPCION" <<endl; 
	//cin.get(1000)>>(descripcion, 1000);
	//cin >> (descripcion);
	cout << "INGRESE LA DISPONIVILIDAD S=SI ESTA N=NO ESTA "<<endl; 
	cin >> disponibilidad;
	cout << "INGRESE EL COSTO DEL PRODUCTO "<<endl; 
	cin >> costo;
	cout << "INGRESE EL PRECIO DEL PRODUCTO"<<endl; 
	cin >> precio;
	cout << "INGRESE LA CANTIDAD DE PRODUCTOS"<< endl;
	cin >> cantidad ; 
	
	system ("cls") ;
	
	//cout << "LOS DATOS INGRESADOS SON LOS SIGUENTES " << endl;
	//cout << "REFERENCIA DEL PRODUCTO ES "<< referencia <<endl;
	//cout << "DESCRIPCION DEL PRODUCTO ES "<< descripcion <<endl;
	//cout << "DISPONIBILIDAD DEL PRODUCTO ES "<< disponibilidad <<endl;
	//cout << "TALLA DEL PRODUCTO ES "<< talla <<endl;
	//cout << "COSTO DEL PRODUCTO ES "<< costo <<endl;
	//cout << "PRECIO DEL PRODUCTO ES "<< precio <<endl;
	
	cout << "LOS DATOS INGRESADOS SON LOS SIGUENTES " << endl;
	
	int dat1=costo-precio ;
	float dat2=dat1*1 ;
	float dat3=(dat2/costo);
	
	cout << "REFERENCIA DEL PRODUCTO ES :"<< referencia <<endl;
	cout << "DISPONIBILIDAD DEL PRODUCTO ES :"<< disponibilidad <<endl;
	cout << "CANTIDAD DE PRODUCTOS ES :" << cantidad <<endl ;
	cout << "TALLA DEL PRODUCTO ES : "<< talla <<endl;
	cout << "COSTO DEL PRODUCTO ES :"<< costo <<endl;
	cout << "COSTO DE UNIDADES DISPONIBLES :" << costo*cantidad << endl;
	cout << "PRECIO DEL PRODUCTO ES : "<< precio <<endl;
	cout << "UTILIDAD DEL PRODUCTO ES :" << abs(costo-precio) <<endl;
	cout << "UTILIDAD DE LAS CANTIDADES DISPONIBLES ES :" << abs((precio-costo)*cantidad)<<endl;
	cout << "PORCENTAJE DE UTILIDAD ES : " << abs(dat3) << endl ;
	
}
