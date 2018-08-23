#!/usr/bin/env python
# -*- coding: 850 -*-
# extraer registros de un archivo txt
# @utor: Leonardo Marcos Santiago

import os
import shutil

def leer_archivo(lista_registros):
	archivo = open("104180818114635_SEND_TRAN05c.xml", "r")
	registro = ""
	for linea in archivo.readlines():
		if(linea != '\n'):
			registro = linea.replace('\n',' ')
			lista_registros.append(registro)
			print(registro)
			registro = ""

def escribir_en_archivo(lista_registros):
    archivo = open('hola.xml','w')
    for registro in lista_registros:
		archivo.write(registro + "\n")
    archivo.close()

def eliminar_lineas_vacias(registros):
	contador = 0
	lista = []
	for linea in registros:
		if(len(linea) != 0):
			lista.append(linea)
	return lista

os.system("reset")
lineas = []
registros = []
leer_archivo(lineas)
registros = eliminar_lineas_vacias(lineas)
escribir_en_archivo(registros)