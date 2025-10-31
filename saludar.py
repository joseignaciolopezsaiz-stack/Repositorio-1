def saludar_es():
    print("hola")
def saludar_en():
    print("Hi")
def saludar_fr():
    print("Salut")
func = {"es": saludar_es,"en": saludar_en,"fr": saludar_fr}
f = func["es"]
f()