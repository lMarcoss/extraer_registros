#!/usr/bin/env python
# -*- coding: 850 -*-
# extraer registros de un archivo txt
# @utor: Leonardo Marcos Santiago

#import os
import shutil

def leer_archivo(lista_registros):
	archivo = open("104180818114635_SEND_TRAN05c.xml", "r")
	registro = ""
	sin_oiis = "<oiis/>"
	oiis_start = "<oiis>"
	oiis_end = "</oiis>"
	registros_oii = False
	for linea in archivo.readlines():
		if(linea != '\n'):
			# TERMINA SI NO HAY REGISTROS OII
			if(sin_oiis in linea):
				print("no existen registros de oiis")
				break
			# LEER SOLO REGISTROS DE OII
			if(oiis_start in linea):
				registros_oii = True
			if(registros_oii == False):
				continue
			#registro = linea.replace('\n',' ')
			registro = linea.strip()
			lista_registros.append(registro)
			# TERMINA SI YA NO HAY REGISTROSS OII
			if(oiis_end in linea):
				registros_oii = False
				break

def escribir_en_archivo(lista_registros):
    archivo = open('oiis.xml','w')
    oiis_start = "<oiis>"
    oiis_end = "</oiis>"
    oii_start = "<oii>"
    oii_end = "</oii>"
    for registro in lista_registros:
    	if(oiis_start in registro or oiis_end in registro):
    		registro_formateado = registro + "\n"
    		#archivo.write(registro + "\n")
    	elif(oii_start in registro or oii_end in registro):
    		registro_formateado = "\t" + registro + "\n"
    		#archivo.write("\t" + registro + "\n")
    	else:
    		registro_formateado = "\t\t" +registro + "\n"
    		#archivo.write("\t\t" +registro + "\n")
    	archivo.write(registro_formateado)
    	print(registro_formateado)
    archivo.close()

def eliminar_lineas_vacias(registros):
	contador = 0
	lista = []
	for linea in registros:
		if(len(linea) != 0):
			lista.append(linea)
	return lista

#os.system("reset")
lineas = []
registros = []
leer_archivo(lineas)
registros = eliminar_lineas_vacias(lineas)
escribir_en_archivo(registros)