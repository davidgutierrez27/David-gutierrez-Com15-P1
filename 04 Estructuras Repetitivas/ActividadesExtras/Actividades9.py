dia = int(input("valor1:"))
mes = int(input("valor2:"))
año = int(input("valor3:"))

if mes in [1,3,5,7,8,10,12]:
    dd=31
elif mes in [4,6,9,11]:
    dd=30
elif mes == 2:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dd = 29
    else:
        dd = 28
else:
    print("A")
    dd=-1

if dd != -1:
    if dia < 1 or dia > dd:
        print("B")
    elif mes < 1 or mes > 12:
        print("C")
    else:
        print("D")