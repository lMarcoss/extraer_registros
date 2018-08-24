#!/usr/bin/env python
# -*- coding: 850 -*-
# extraer registros de un archivo txt
# @utor: Leonardo Marcos Santiago

import os
import sys
import shutil

def leer_archivo(lista_registros, file_xml):
	archivo = open(file_xml, "r")
	registro = ""
	sin_oiis = "<oiis/>"
	oiis_start = "<oiis>"
	oiis_end = "</oiis>"
	registros_oii = False
	print(file_xml)
	for linea in archivo.readlines():
		if(linea != '\n'):
			if("<oiis><oii>" in linea):
				start = linea.find("<oiis>")
				end = linea.find("</oiis>")
				data_start = linea[:start]
				data_end = linea[end+7:]
				#print(data_start)
				#print(data_end)
				oii_data = linea.replace(data_end, '')
				oii = oii_data.replace(data_start, '')
				oii = oii.replace("<oiis>", "<oiis>\n").replace("<oii>", "<oii>\n").replace("</code>", "</code>\n").replace("</description>", "</description>\n").replace("</oii>", "</oii>\n")
				output_in_file(oii, file_xml)
				leer_archivo_oii(lista_registros, "oii_"  + file_xml)

def leer_archivo_oii(lista_registros, file_xml):
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

def output_in_file(data, file_a):
	file_out = open("oii_"  + file_a , "w")
	file_out.write(data)
	file_out.close()

def escribir_en_archivo(lista_registros, file_xml):
	if(len(lista_registros)>0):
		name_file_output = file_xml.replace(".xml", "_oiis.xml")
		archivo = open(name_file_output,'w')
		oiis_start = "<oiis>"
		oiis_end = "</oiis>"
		oii_start = "<oii>"
		oii_end = "</oii>"
		rows_oiis = []
		row_oii = []
		start_oii = False
		solicitud = file_xml[:file_xml.find("_RECEIVED")] 
		print(solicitud)
		print("----------------")
		print("ROWS: ", len(lista_registros))

		for registro in lista_registros:
			if(len(row_oii) == 0):
				row_oii.append(solicitud)
			if(oiis_start in registro or oiis_end in registro):
				registro_formateado = registro + "\n"
			elif(oii_start in registro or oii_end in registro):
				registro_formateado = "\t" + registro + "\n"
				if(start_oii == False):
					start_oii = True
					if(len(row_oii) == 3):
						rows_oiis.append(row_oii)
					row_oii = []
				if(start_oii == True):
					start_oii = False
			else:
				registro_formateado = "\t\t" +registro + "\n"
				if("code" in registro):
					code = registro.replace("<code>", '').replace("</code>", '')
					row_oii.append(code)
				if("<description>" in registro):
					description = registro.replace("<description>", '').replace("</description>", '')
					row_oii.append(description)
			archivo.write(registro_formateado)
			print(registro_formateado.replace('\n', ''))
		archivo.close()
		return rows_oiis

def obtener_registros_oii_archivo(name_file_input):
	lineas = []
	registros = []
	leer_archivo(lineas, name_file_input)
	rows = escribir_en_archivo(lineas, name_file_input)
	return rows
	#obtener_datos_oii_por_separado(lineas, registros)
	#escribir_en_archivo_oii(registros)


def print_in_csv(rows):
    file_oii = open('oiis_output.csv','w')
    for registro in rows:
    	for x in registro:
    		print(x[0])
    		print(x[1])
    		print(x[2])
    		file_oii.write(x[0] + ", " + x[1]+ ", " + x[2].replace(',','') + "\n")
	#file_oii.close()

#os.system("reset")
listado = os.listdir(os.getcwd())
extension = ".xml"
nuevo_negocio = "RECEIVED_TRAN05c.xml"
inclusion = "RECEIVED_TRAN39e.xml"
incremento = "RECEIVED_TRAN08g.xml"

datos = []
for elemento in listado:
	if(os.path.isfile(elemento) and (nuevo_negocio in elemento or inclusion in elemento or incremento in elemento)):
		print("--> %s es un archivo" % elemento)
		data = obtener_registros_oii_archivo(elemento)
		if data is not None:
			datos.append(data)
print(datos)
print_in_csv(datos)

