import csv

# Cargar los datos desde los archivos CSV
with open('categorias.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    categorias = list(reader)

with open('productos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    productos = list(reader)

categorias_dict={}
print('categorias')
for categoria in categorias[:200]:
    print(categoria)
    categorias_dict[categoria['id']]=categoria['modelo']

print('union')

for c in categorias_dict:
    print(f'id:{c} | valor:{categorias_dict[c]}')
    
print(categorias_dict['200'])

productos_dict={}
print('productos')
for producto in productos[:1000]:
    print(producto)
    productos_dict[producto['id']]={'nombre': categorias_dict[producto['id_categoria']],'productos':producto['marca'],
    'precio':producto['precio'],'unidades_disponibles': producto['unidades_disponibles'],'id_categoria':producto['id_categoria']}
    

print('union')

for r in productos_dict:
    print(f'id:{r} | valor:{productos_dict[r]}') 