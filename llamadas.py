def llamada1(a,b) :
     print("llamada1")
     print(a,b)
def llamada2(a,b):
     print("llamada2")
def llamada3(a,b):
    print("llamada3")
def llamada4(a,b):
   print("llamada4")
def llamada5(a,b):
    print("llamada5")
def llamada6(a,b):
    print("llamada7")
def llamada7(a,b):
    print("llamada7")
def llamada8(a,b):
    print("llamada8")
dicc = {
            '0': llamada1,
            '1': llamada2,
            '2': llamada3,
            '3': llamada4,
            '4': llamada5,
            '5': llamada6,
            '6': llamada7,
            '7': llamada8,}
f = dicc["6"]
f("hola","soy yo")
            