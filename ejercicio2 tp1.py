#!/usr/bin/python3

import sys
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Programa para copiar archivos.')

parser.add_argument('-i', '--input', type=str, help='Nombre del archivo de entrada.', required=True)
parser.add_argument('-o', '--output', type=str, help='Nombre del archivo de salida.', required=True)

args = parser.parse_args()

if not os.path.exists(args.input):
    print(f'El archivo {args.input} no existe en el disco.')
    exit(1)
    
with open(args.input, 'r') as input_file:
    input_content = input_file.read()

with open(args.output, 'w') as output_file:
    output_file.write(input_content)

print(f'Se ha copiado el contenido de {args.input} a {args.output}.')
