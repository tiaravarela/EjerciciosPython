def ejercicio1():


    print("ingrese un primer numero")
    num1=int(input())


    print("ingrese un segundo numero")
    num2=int(input())


    r = num1 + num2


    print("el resultado es: ",r)



def ejercicio2():


    print("ingrese un primer numero")
    num1=int(input())


    print("ingrese un segundo numero")
    num2=int(input())


    print("ingrese un tercer numero")
    num3=int(input())


    print("ingrese un cuarto numero")
    num4=int(input())


    r = num1 + num2 + num3 + num4


    print("el resultado es: ",r)



def ejercicio3():


    print("ingrese la altura del rectangulo")
    altura=int(input())


    print("ingrese la base del rectangulo")
    base=int(input())


    s = altura * base


    print("la superficie del rectangulo es: ",s)



def ejercicio4():


    print("ingrese un lado del cuadrado con decimal")
    lado= float(input())


    s = lado * lado


    print("la superficie del cuadrado es: ",s)



def ejercicio5():


    print("ingrese una hora")
    hora=int(input())


    print("ingrese minutos")
    minutos=int(input())


    print("ingrese segundos")
    segundos=int(input())


    r= hora * 60 * 60 + minutos * 60 + segundos


    print("el resultado en segundos es: ",r)



def ejercicio6():


    print("ingrese la altura del triangulo")
    altura=int(input())


    print("ingrese la base del triangulo")
    base=int(input())


    s = altura * base / 2


    print("la superficie del triangulo es: ",s)



def ejercicio7():


    print("ingrese un primer numero")
    num1=int(input())


    print("ingrese un segundo numero")
    num2=int(input())


    print("ingrese un tercer numero")
    num3=int(input())


    print("ingrese un cuarto numero")
    num4=int(input())


    print("ingrese un quinto numero")
    num5=int(input())


    print("ingrese un sexto numero")
    num6=int(input())


    print("ingrese un septimo numero")
    num7=int(input())


    suma= num1 + num2 + num3 + num4 + num5 + num6 + num7

    p= suma / 7


    print("el promedio es: ",p)




def ejercicio8():


    print("ingrese un numero parcial")
    num1=int(input())


    print("ingrese un numero total")
    num2=int(input())


    p= num1 * 100 / num2


    print("el porcentaje es: ",p)



def ejercicio9():


    print("ingrese una fecha en formato DDMMAAAA sin barras")
    fecha=int(input())


    año = fecha % 10000


    mes = fecha // 10000 % 100


    dia = fecha // 1000000


    print("dia: ", dia)
    print("mes: ", mes)
    print("año: ", año)



def ejercicio10():


    print("ingrese una nota de examen entre 0 y 10")
    nota1=int(input())


    print("ingrese una nota de TP entre 0 y 10")
    nota2=int(input())


    print("ingrese una nota de examen integrador entre 0 y 10")
    nota3=int(input())


    notafinal = nota1 * 30 / 100 + nota2 * 20 / 100 + nota3 * 50 / 100


    print("la nota final es: ",notafinal)



def ejercicio11():


    print("ingrese la cantidad de autos vendidos")
    cantidad=int(input())


    print("ingrese el valor de los autos")
    valor=float(input())


    salariototal = 5500 + 200 * cantidad + valor * 5 /100


    print("el salario total es: ",salariototal)

