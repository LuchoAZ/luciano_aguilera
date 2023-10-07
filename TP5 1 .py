"""#eje 1

def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False




while True:
    try:
        dni = int(input("Ingrese su DNI: "))
        print(validDni(dni))
        break
    except ValueError:
        print("Por favor ingrese un numero de DNI válido")
#eje 2

def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if palabras:
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:
        return 0
#eje 3

#validar DNI
def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False
#Buscar apellido
def searchLastName(entryName):
    if len(entryName) >= 3:
        return  entryName[2]
    elif len(entryName) == 2:
        return entryName[1]
    #Obtener los primero 3 números del dni
def getDniId(dni):
    if len(str(dni)) == 8:
        return dni // 100000
    else:
        return dni // 10000


def createId(name, lastName, numId):
    prevId = ""
    prevId += name[0] + str(len(lastName)) + str(numId)
    import aFunciones as funcion
try:
    while True:
        vDni = False
        fullName = input("Ingrese el nombre completo del socio. \nPara finalizar y salir ingrese un epacio en blanco: ")
        fullName = fullName.split()
        if fullName == "" or fullName == " ":
            break
        if len(fullName) < 2:
            print("Ingrese al menos 1 nombre y 1 apellido")
        else:
            while vDni == False:
                try:
                    dni = int(input("Ingrese su DNI: "))
                    vDni = funcion.validDni(dni)
                    if vDni == False:
                        print("Ingrese un DNI válido")
                except ValueError:
                    print("Ingrese carácteres válidos para la correcta ejecución")
            lastName = funcion.searchLastName(fullName)
            dniId = funcion.getDniId(dni)
            finalId = funcion.createId(fullName, lastName, dniId)


            print(f" Nombre: {' '.join(fullName)} \n DNI: {dni} \n ID: {finalId}")
            print("Adios.")
except ValueError:
    print("Ingrese carácteres válidos para la correcta ejecución")
#eje 4 

a = int(input('Ingresa el primer numero: '))
print()
b = int(input('Ingresa el segundo numero: '))
def Multiples(a,b):
  if a % b == 0:
    print(f'El primer numero: {a} es multiplo del segundo numero: {b}')

Multiples(10,2)

print()
if a % b == 0:
  print(f'{a} es multiplo de {b}')
if b % a == 0:
  print(f'{b} es multiplo de {a}')
#eje 5

def calc_median(max, min):
    median = (max + min) / 2
    return median
import aFunciones as funcion
cant_days = int(input("Ingrese la cantidad de días a los que se les va a calcular la media de temperatura: "))
for i in range(0, cant_days):
    temp_max = float(input(f"Ingrese la máxima en °C del día {i + 1}: "))
    temp_min = float(input(f"Ingrese la mínima en °C del día {i + 1}: "))
    median = funcion.calc_median(temp_max, temp_min)
    print(f"La media del día {i + 1} es : {median}°C")
#eje 6

def space_between_letters(word):
    # Use compresion de listas para hacer este código.
    spaced_word = ''.join([c + ' ' for c in word if c != ' '])
    return spaced_word
from tp5 import *
import pytest
def space_word_test():
  assert space_between_letters('Hola, tu') == 'H o l a, t u'
#eje 7

def calc_min_and_max(num_list):
    n_min = 100000000000000000
    n_max = 0
    for i in range(len(num_list)):
        if num_list[i] < n_min:
            n_min = num_list[i]
        elif num_list[i] > n_max:
            n_max = num_list[i]
    return n_min, n_max
import aFunciones as funcion
num_list = []
while True:
    try:
        while True:
            entry_num = (input("Ingrese números. Para deterse y mostrar el máxumo y el mínimo ingrese 'Salir': ")).lower()
            if entry_num == "salir":
                break
            else:
                num_list.append(int(entry_num))
            min, max = funcion.calc_min_and_max(num_list)
        print(f"El número ingresado mas bajo es: {min}. \nEl número ingresado mas alto es {max}.")
        break
    except ValueError:
        print("Ingrese un num")
#eje 8

import math
def calc_circumference(circumference):
    circumference = float(circumference)
    radius =  circumference / (2 * math.pi)
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return radius, area, perimeter


print('Calculadora de area, radio y perimetro en base a la circunferencia de un circulo.\n')


circumference = input('Ingrese la circunferencia del círculo: \n')


radius, area, perimeter = calc_circumference(circumference)


print(f'El radio del círculo es: {radius}\nSu área es {area}\nSu perímetro es: {perimeter}')
##-------------------Ejercicio 9 ------------------------------------------------
#función
def login(user, password):
    login_ok = 0
    if user == "usuario1" and password == "asdasd":
        login_ok = 1
   
    return login_ok




#programa principal
print("Bienvenido: ")


exit = 0
while exit < 3:
    user = input("Por favor ingrese su usuario: ")
    password = input("Por favor ingrese su contraseña: ")
    login_ok = login(user,password)
    if login_ok == 1:
        break
    else:
        print("Datos ingresados incorrectos. ")
    exit +=1


if login_ok == 1:
    print("Bienvenido: ")
else:
    print("Usted asuperado el número de intentos permitidos para ingresar, por favor reintente luego. ")
#eje 10

def purchase_total(prices_percentages):
    prices=list(prices_percentages.keys())
    percentages=list(prices_percentages.values())
    total=0
    for n in range(len(prices)):
        calculation=prices[n]*(1-percentages[n])
        total+=calculation
    return total




prices_percentages= [2500:0.15,3000:0.20,1500:0.05,2600:0.30,6740:0.25,2000:0.10]

print(f"El total de la compra con los respectivos descuentos es de: {purchase_total(prices_percentages)}")


#PYTEST
import pytest
from prueba import *
@pytest.mark.parametrize('a,res',[
    ({1000:0.10,2000:0.20,3000:0.30,1500:0.10,2500:0.20,3500:0.30},10400),
    ({1500:0.15,2500:0.25,3500:0.35,1550:0.15,2550:0.25,3550:0.35},10962.5)
])
def test_purchase_total(a,res):
    assert purchase_total(a)==res
#eje 11

#funcion
def swap(names):
    apply_change = ""
    apply_change = names.swapcase()
    return apply_change


def call_other_f(names):
    change_name = ""
    change_name = swap(names)
    return change_name
#codigo principal


names = ["JuAn ", "AMeLia ", "AnToNellA "]


for i in range(3):
    print("Elemento de la lista antes de la funcion: ", names[i])


    print("Llamamos la funcion. ")


    names[i] = call_other_f(names[i])
   
    print("Elemento de la lista después de la funcion: ", names[i])

#eje 12

def phrase_to_dict(phrase):
    new_dict = {}
    temporal_array = phrase.split(" ")
    for word in temporal_array:
        new_dict[word] = len(word)
    return new_dict
#eje 13

import math
def calc_modulo_vector(array):
    aux_sum = 0
    for i in array:
        aux_sum += i**2
    modul = math.sqrt(aux_sum)
    return modul

import aFunciones as funcion
vector = [


]
dimension = 3
for i in range(dimension):
    valor = int(input(f"Ingrese el valor para la componente {i + 1}: "))
    vector.append(valor)
vector_modul = funcion.calc_modulo_vector(vector)
print(f"El módulo del vector es: {vector_modul}")
#eje 14

def verify_prime_number(num):
    divisors = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            divisors += 1
    if divisors <= 2:
        return True
    else:
        return False
        import aFunciones as funcion
new_num = int(input("Ingrese un número: "))
prime_num = funcion.verify_prime_number(new_num)
if prime_num == True:
    print("El número es primo")
else:
    print("El número no es primo")
#eje 15

def calc_factorial(num):
    fact = 1
    if num == 0:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact *= i
    return fact


def calc_entries(aux_num):
    if aux_num >= 0:
        return 1
import aFunciones as funcion
cant_entries = 0
while True:
        #try:
            num_fact = int(input("Ingrese un número para saber su factorial. \nIngrese un número negativo para parar: "))
            if num_fact < 0:
                break
else:
    
#factorial = funcion.calc_factorial(num_fact)

cant_entries += funcion.calc_entries(factorial)
print(f"el factorial del número {num_fact} es: {factorial}")

#except ValueError:

print("Ingrese un número")
print(f"Usted ha calculado los factoriales de {cant_entries} números")
#eje 16 
def separate_num(num):
    aux = list(str(num))
    return aux


def determ_frec(dig, frec, separate_num):
    for i in separate_num:
        if dig == i:
            frec +=1
    return frec
#import aFunciones as funcion
try:
    frecuency = 0
    num = int(input("Ingrese un número entero: "))
    #separar el número
    num = funcion.separate_num(num)
    while True:
        digit = (input("Ingrese un dígito: "))
        if len(digit) > 1:
            print("Ingrese solamente un dígito")
        else:
            break
    frecuency = funcion.determ_frec(digit, frecuency, num)
    print(f"El número {digit} aparece {frecuency} veces en el número {('').join(num)}")
except ValueError:
    print("Ingrese solamente números")
#eje 17

import math
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True




def entering_prime_numbers():
    most_number = 0
    while True:
     num = int(input('Ingresa un numero primo, la lectura finalizara cuando ingreses un numero no primo:\n'))
     if is_prime(num):
            prime_sum = 0
            digit_frecuence = 0
            for digit in str(num):
                prime_sum += int(digit)
            print(f'La suma de los digitos del numero primo ingresado es: {prime_sum}')
            opt_frecuence = input('Ingresa un digito del cual quieres saber la frecuencia en el numero ingresado:\n')
            for digit in str(num):
                if digit == opt_frecuence:
                    digit_frecuence += 1
            if num > most_number:
                most_number = num
            print(f'La frecuencia del digito "{opt_frecuence}" en "{num}" es: {digit_frecuence}')
     else:
        print(f'El numero ingresado no es primo, el mayor numero que ingresaste en esta sesion fue "{most_number}"  y su factorial es: {math.factorial(most_number)}\n Saliendo...')
        break


entering_prime_numbers()"""