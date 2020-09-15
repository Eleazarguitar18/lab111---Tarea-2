print("ingrese la hora porfavor")
h=int(input())
print("Ingrese los minutos porfavor")
m=int(input())
print("ingrese los segundos pofavor")
s=int(input())
print("¿cuantos segundos desea sumar?")
sumaseg=int(input())
s=s+sumaseg
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
print("la hora con los segundos sumados es: ")            
print(format(h, '02'),":",format(m, '02'),":",format(s, '02'))
#Eleazar Jhonny Cruz Mamani
