#!/usr/bin/env python
# -*- coding: 850 -*-
# extraer registros de un archivo txt
# @utor: Leonardo Marcos Santiago

#import os
import sys
import shutil

def leer_archivo(lista_registros, file_xml):
	archivo = open(file_xml, "r")
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

def escribir_en_archivo(lista_registros, file_xml):

	name_file_output = file_xml.replace(".xml", "_oiis.xml")
	archivo = open(name_file_output,'w')
	oiis_start = "<oiis>"
	oiis_end = "</oiis>"
	oii_start = "<oii>"
	oii_end = "</oii>"
	for registro in lista_registros:
		if(oiis_start in registro or oiis_end in registro):
			registro_formateado = registro + "\n"
		elif(oii_start in registro or oii_end in registro):
			registro_formateado = "\t" + registro + "\n"
		else:
			registro_formateado = "\t\t" +registro + "\n"
		archivo.write(registro_formateado)
		print(registro_formateado.replace('\n', ''))
	archivo.close()

#os.system("reset")
if(len(sys.argv) < 2):
	print("Es necesario el nombre del archivo a leer")
else:
	name_file_xml = sys.argv[1]
	extension = ".xml"
	#name_file = file_xml
	if(extension not in name_file_xml):
		name_file_xml = name_file_xml + extension
	lineas = []
	registros = []
	leer_archivo(lineas, name_file_xml)
	escribir_en_archivo(lineas, name_file_xml)