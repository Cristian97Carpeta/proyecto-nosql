import csv

# Cargar los datos desde los archivos CSV
with open('categorias.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    categorias = list(reader)

with open('productos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    productos = list(reader)


categorias_dict = {}
print ("CATEGORIAS")
for categoria in categorias[:5]:
    categorias_dict[categoria["id"]] = categoria["modelo"]
    print(categoria)
    categorias_dict[categoria["id"]]= {"nombre": categoria["modelo"], "productos": []}


print(categorias_dict)



print("PRODUCTOS")
productos_dict={}

for producto in productos:
    productos_dict[producto["id"]] = {producto["marca"],producto["precio"],producto["unidades_disponibles"]}
    categorias_dict



