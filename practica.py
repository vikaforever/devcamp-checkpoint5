# 1.  Cree un bucle For de Python.

for num in range(1, 100): #[1, 2, 3...., 99]
    print(num)
    print(num + 1)


# 2. Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

print(suma(1, 2, 3))

# 3. Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda arg1, arg2, arg3: arg1 + arg2 + arg3

print(suma(4, 5, 6))

# 4. Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 

nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
if nombre in lista_nombre: 
    print('True')
else: 
    print('False')