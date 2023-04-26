#!/usr/bin/python

import sys
import getopt


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return num1 / num2


def calcular(operador, num1, num2):

    operadores = {
        '+': sumar,
        '-': restar,
        '*': multiplicar,
        '/': dividir
    }

    if operador not in operadores:
        raise ValueError("Operador inválido.")

    funcion = operadores[operador]
    return funcion(num1, num2)


def validar_argumentos(args):

    valid_operadores = ['+', '-', '*', '/']
    operador = None
    num1 = None
    num2 = None

    try:
        opts, _ = getopt.getopt(args, "o:n:m:")
    except getopt.GetoptError as e:
        raise ValueError(str(e))

    for opt, arg in opts:
        if opt == '-o':
            if operador is not None:
                raise ValueError("El operador está repetido.")
            if arg not in valid_operadores:
                raise ValueError("Operador inválido.")
            operador = arg
        elif opt == '-n':
            if num1 is not None:
                raise ValueError("El primer número está repetido.")
            try:
                num1 = int(arg)
            except ValueError:
                raise ValueError("El primer número no es un entero.")
        elif opt == '-m':
            if num2 is not None:
                raise ValueError("El segundo número está repetido.")
            try:
                num2 = int(arg)
            except ValueError:
                raise ValueError("El segundo número no es un entero.")

    if operador is None or num1 is None or num2 is None:
        raise ValueError("Faltan argumentos.")

    return {'operador': operador, 'num1': num1, 'num2': num2}


if __name__ == '__main__':
    try:
        datos = validar_argumentos(sys.argv[1:])
        resultado = calcular(datos['operador'], datos['num1'], datos['num2'])
        print(f"{datos['num1']} {datos['operador']} {datos['num2']} = {resultado}")
    except ValueError as e:
        print(f"Error: {str(e)}")



