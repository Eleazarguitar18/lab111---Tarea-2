#Utilizando los coeficientes (a, b, c) de una ecuación de segundo grado
#se pide mostrar la naturaleza de sus raíces
print("ingresa el coeficiente de la variable cuadratica: ")
a=int(input())
print("ingresa el coeficiente de la variable lineal: ")
b=int(input())
print("ingresa el numero independiente: ")
c=int(input())
if((b**2-4*a*c)<0):
    print("la solucion es con numeros complejos ")
else:
    x1=((-1)*b+((b**2-4*a*c)**(1/2)))/(2*a)
    x2=((-1)*b-((b**2-4*a*c)**(1/2)))/(2*a)
    print("las soluciones son numeros racionales y son:" )
    print("x1= ", x1)
    print("x2= ", x2)
#ELEAZAR JHONNY CRUZ MAMANI
