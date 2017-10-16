#!/usr/bin/env python
# -*- coding: 850 -*-
# Crear pares de autores de una publicación de artículo o libro
# @utor: Leonardo Marcos Santiago

#import os
import shutil

def leer_archivo(lista_registros):
	archivo = open("arch.txt", "r")
	registro = ""
	for linea in archivo.readlines():
		if(linea != '\n'):
			registro = registro + linea
		else:
			registro = registro.replace('\n',' ')
			lista_registros.append(registro)
			registro = ""
def escribir_en_archivo(lista_registros):
    archivo = open('capturas1.csv','w')
    for registro in lista_registros:
		archivo.write(registro[0] + ", " + registro[1]+ ", " + registro[2]+ ", " + registro[3] + "\n")
    archivo.close()


def llenar_paises():
	paises = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Cocos", "Colombia", "Comoros", "Democratic Republic of the Congo", "Kinshasa", "Congo, Republic", "Congo", "Republic of Congo", "Cook Islands", "Costa Rica", "Ivory Coast ", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Timor-Lest", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Great Britain", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Rep. (North Korea)", "Korea, Republic of (South Korea)", "South Korea", "North Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Lao", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar, Burma", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Palestinian territories", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn Island", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion Island", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovak ", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Tibet", "Timor", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "Emirates Arab", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State (Holy See)", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"]
	return paises

def eliminar_lineas_vacias(registros):
	contador = 0
	lista = []
	for linea in registros:
		if(len(linea) != 0):
			#contador = contador + 1
			# print("registro " + str(contador))
			#print(linea)
			lista.append(linea)
	return lista

def extraer_datos(registros,paises):
	lista_datos = []
	for registro in registros:
		lista_datos.append(detalle_registro(registro,paises))
	escribir_en_archivo(lista_datos)

def buscar_pais(registro,paises):
	countrie = "XXXXX"
	for pais in paises:
		if(pais in registro):
			countrie = pais
			break
	return countrie

# def buscar_nombre(registros):
# 	for registro in registros:
# 		if(tiene_alias(registro)):
# 			print('')
			#extraer_alias(registro)
		#if('(' in registro):

		#	print(registro.index('('))
		#else:
		#	print("no hay parantesis")
def es_pais(alias, paises):
	es_pais = False
	for pais in paises:
		if(alias == pais):
			es_pais = True
			# print("paisSSSssssssssslllllpaisSSSssssssssslllllpaisSSSssssssssslllllpaisSSSssssssssslllll")
			break
	return es_pais

def tiene_alias_dif_individual(registro,paises):
	tiene_alias = False
	parantesis_ini = 0
	parentesis_fin = 0
	alias = "XXXXX"
	if('(' in registro ):
		parantesis_ini = registro.find('(')
		parentesis_fin = registro.find(')')
		alias = registro[parantesis_ini+1 : parentesis_fin]
		if(alias != 'individual' and not es_pais(alias,paises)):
			tiene_alias = True
		# else:
		# 	print("es individual o es pais _>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		# 	print("::::::::::::::::::::::::")
		# 	print(registro)
		# 	print("::::::::::::::::::::::::")
		# 	print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
	return tiene_alias


def tiene_alias(registro,paises):
	alias = False
	posicion_parentesis = 0
	posicion_dob = 0
	posicion_pod = 0
	if('(' in registro):
		posicion_parentesis = registro.find('(')

	if('DOB' in registro):
		posicion_dob = registro.find('DOB')

	if('POB' in registro):
		posicion_dob = registro.find('POB')

	if(posicion_parentesis < posicion_dob or posicion_parentesis < posicion_pod):
		alias = True
	else:
		if(tiene_alias_dif_individual(registro,paises)):
			alias = True
		else:
			alias = False

	return alias

def extraer_alias(registro):
	alias = "XXXXX"
	if(tiene_alias(registro,paises)):
		parentesis_ini = registro.find('(')
		parentesis_fin = registro.find(')')
		alias = registro[parentesis_ini +1: parentesis_fin]
	# else:
	# 	print(registro)
	return alias

def extraer_nombres(registro,paises):
	nombre_completo = "XXXXX"
	primer_parentesis = 0
	if(tiene_alias(registro,paises)):
		primer_parentesis = registro.find('(')
		nombre_completo = registro[0: primer_parentesis]
	return nombre_completo

def es_individual(registro):
	if("individual" in registro):
		return True
	else:
		return False

def detalle_registro(registro,paises):
	detalle = []
	countrie = buscar_pais(registro,paises)
	alias = extraer_alias(registro)
	nombre_completo = extraer_nombres(registro,paises)
	first_name = ""
	last_name = ""
	nombres = []
	minimo = 0
	pos_coma = 0
	pos_punto_coma = 0
	if(nombre_completo != "XXXXX"):#tiene alias
		nombres = nombre_completo.split(",")
		first_name = nombres[0].strip()
		if(len(nombres) > 1):
			last_name = nombres[1].strip()
	else:#individual
		if (es_individual(registro)):
			primer_coma = registro.find(",")
			first_name = registro[0: primer_coma]
			registro = registro.replace(first_name + ",", "")
			pos_coma = registro.find(",")
			pos_punto_coma = registro.find(";")
			if(pos_coma < pos_punto_coma and pos_coma > 0):
				minimo = pos_coma
			if(pos_punto_coma < pos_coma and pos_punto_coma > 0 ):
				minimo = pos_punto_coma
			print(minimo)
			last_name = registro[0: minimo]
			# first_name = nombres[0].strip()
			# if(len(nombres) > 1):
			# 	last_name = nombres[1].strip()
		else:
			primer_coma = registro.find(",")
			first_name = registro[0: primer_coma]
	if(first_name == "XXXXX"):
		first_name = '';
	if(last_name == "XXXXX"):
		last_name = '';
	if(alias == "XXXXX"):
		alias = '';	
	if(countrie == "XXXXX"):
		countrie = '';
	detalle.append(first_name.replace(';','').replace(',','').replace('','').replace('a.k.a.','').replace('"','').replace('  ', ' ').replace("'",' ').strip())
	detalle.append(last_name.replace(';','').replace(',','').replace('','').replace('a.k.a.','').replace('"','').replace('  ', ' ').replace("'",' ').strip())
	detalle.append(alias.replace(';','').replace(',','').replace('','').replace('a.k.a.','').replace('"','').replace('  ', ' ').replace("'",' ').strip())
	detalle.append(countrie.replace(';','').replace(',','').replace('','').replace('a.k.a.','').replace('"','').replace('  ', ' ').replace("'",' ').strip())
	return detalle


	
# os.system("reset")
paises = []
lista_persona_fisicas = []
lista_personas_morales = []
lineas = []
registros = []
leer_archivo(lineas)
paises = llenar_paises()
registros = eliminar_lineas_vacias(lineas)
extraer_datos(registros,paises)
#buscar_pais(registros,paises)
#buscar_nombre(registros)
