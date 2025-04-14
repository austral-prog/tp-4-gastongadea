def leap_year():
    anio=int(input("Ingrese un año: "))
    if anio/4==anio//4:
        if anio/100==anio//100 and anio/400==anio//400:
            print(f"El año {anio} es bisiesto")
        else:
            print(f"El año {anio} no es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
