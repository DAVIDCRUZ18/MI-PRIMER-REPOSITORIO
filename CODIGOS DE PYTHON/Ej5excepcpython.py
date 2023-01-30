#5. Excepciones personalizadas
# En ocasiones, es posible que necesite crear excepciones personalizadas que sirvan a su propósito.
# En Python, los usuarios pueden definir tales excepciones creando una nueva clase. 
# Esta clase de excepción debe derivarse, directa o indirectamente, de la clase Excepción. 

class ErrorValorMuyPeque(Exception):
        """Raised when the input value is too small"""
        pass

numero = 10

while True:
    try:
        num_usuario = int(input("Ingrese un número: "))
        if num_usuario < numero:
            raise ErrorValorMuyPeque
        break
    except ErrorValorMuyPeque:
            print("Este valor es muy pequeño!")