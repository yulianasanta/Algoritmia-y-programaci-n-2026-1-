a = float(input("ingrese un número: "))
b = float(input("ingrese otro número: "))
c = operador = input("ingrese el operador que desea usar: +, -, *, /: ")

if c == "+":
    print (f"{a} + {b} = {a+b}")
elif c=="-":
    print (f"{a} - {b} = {a-b}")
elif c=="*":
    print (f"{a} * {b} = {a*b}")
elif c=="/":
    if b != 0:
        print (f"{a} / {b} = {a/b}")
    else:
        print("Error: No se puede dividir por cero.")