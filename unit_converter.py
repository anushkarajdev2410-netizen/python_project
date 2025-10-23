 # UNIT_CONVERTER

x = input("Enter SI unit : ").strip().lower()

if x == "length":
    a = int(input("Enter length in metres :  "))
    print(a * 100, "centimetre")
    print(a * 1000, "millimetre")
    print(a * 0.001, "kilometre")
    print(a * 39.3700, "inches")
    print(a * 3.28085, "feet")
    print(a * 1.093613, "yard")
    print(a * 0.0006213, "miles")

elif x=="mass":
    b=int(input("Enter Mass in Kilograms : "))
    print(b*0.001, "tons")
    print(b*2.20462, "pounds")
    print(b*35.27396,"Ounces")
    print(b*1000, "grams")

elif x=="area":
    c=int(input("Enter Area in metre square : "))
    print(c*0.0002471, "acres")
    print(c*0.01, "ares")
    print(c*0.0001, "hectares")
    print(c*10000, "centimetre square")
    print(c*1550.0031, "square inch")
    print(c*10.7639, "square feet")

elif x=="volume":
    d=int(input("Enter Volume in metre cube : "))
    print(d*1000, "litres")
    print(d*1000000, "millilitres")
    print(d*1000000, "centimetre cube")
    print(d*61023.744, "inch cube")
    print(d*35.3146667, "feet cube")

elif x=="temp":
    e=int(input("Enter Temperature in Kelvin : "))
    print(e-272.15, "celsius")
    print((e*-273.15)*9/5 + 32, "fahrenheit")

elif x=="time":
    f=int(input("Enter time in seconds : "))
    print(f*1000, "ms")
    print(f/60, "minute")
    print(f/3600, "hour")
    print(f/86400, "day")
    print(f/604800, "week")
    
elif x=="currency":
    g=int(input("Enter INR : "))
    print(g*0.011, "USD")
    print(g*0.0098, "EURO")
    print(g*1.74, "JPY")
    print(g*0.0085, "GBP")
    print(g*0.042, "DIRHAM")

elif x=="data":
    h=int(input("Enter data in kilobytes : "))
    print(h*8000, "bits")
    print(h*1000, "bytes")
    print(h*0.001, "megabytes")
    print(h*0.000001, "gigabytes")

else:
    print("Enter Valid Unit")
  
    