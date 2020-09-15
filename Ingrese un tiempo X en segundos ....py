#ingrese un tiempo X que estará representado en segundos, luego ingrese el tiempo que tomará
#en realizarse una tarea Z representado en segundos, minutos y horas. Se pide verificar si con el
#tiempo X se puede finalizar la tarea Z
print("ingrese el tiempo limite para la tarea (en segundos): ")
x=int(input())
print("ingrese el tiempo que durar la tarea")
print("ingrese la hora porfavor")
h=int(input())
print("Ingrese los minutos porfavor")
m=int(input())
print("ingrese los segundos pofavor")
s=int(input())
print("la tarea durara: ")
if(s>59):
    p=s//60
    s=s%60
    m=m+p
    if(m>59):
        q=m//60
        m=m%60
        h=h+p
        if(h>23):
            t=h//24
            h=h%24
print(format(h, '02'),":",format(m, '02'),":",format(s, '02'))
h=h*3600
m=m*60
z=h+m+s
#print("")
if(x>=z):
    print("si se puede acabar la tarea por que esta dentro del tiempo limite")
else:
    print("la tarea no se puede acabar por que exede el tiempo limite")    
#ELEAZAR JHONNY CRUZ MAMANI
