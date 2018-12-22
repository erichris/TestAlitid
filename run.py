from fichero import Fichero
from sqlite import Database
import time
import datetime

db = Database()
    
#db.crear_conexion("5432", "Playeras", "postgres", "Nomorelove12")
db.crear_conexion("5432", "alitid", "alitid_1", "Nomorelove12")

doc = Fichero();



codigoPromesas = "Promesas"
codigoPlanDeEscape = "PlanDeEscape"
time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


fichero = doc.abrir_fichero("CodigosP00.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPromesas
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()


fichero = doc.abrir_fichero("CodigosP01.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPromesas
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()



fichero = doc.abrir_fichero("CodigosP02.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPromesas
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()



fichero = doc.abrir_fichero("CodigosP03.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPromesas
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()



fichero = doc.abrir_fichero("CodigosP04.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPromesas
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()



fichero = doc.abrir_fichero("Codigos00.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPlanDeEscape
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()

fichero = doc.abrir_fichero("Codigos01.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPlanDeEscape
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()

fichero = doc.abrir_fichero("Codigos02.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPlanDeEscape
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()

fichero = doc.abrir_fichero("Codigos03.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPlanDeEscape
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()

fichero = doc.abrir_fichero("Codigos04.txt", doc.lectura)

for linea in fichero:
	dol = linea.split()
	user = dol[0]
	password = dol[1]
	app = codigoPlanDeEscape
	command = """INSERT INTO public."Login_planescape" ("ID1", "ID2", created, used, app, "ID_Movil1", "ID_Movil2", "ID_Movil3") VALUES ('""" + user +  "', '" + password + "', '" + time + "', '" + "false" + "', '" + app + "', '" + "" +"', '" + "" +"', '" + "" + "');"
	print command
	db.cursor.execute(command);
	db.connection.commit()





    
#db.cursor.execute("UPDATE Comidas set Guarnicion = 'Arroz|Frijoles|Spagethi|Dummy' where DB_ID = 2");
    
#DB_ID = db.obtener_registro("Users", ["DB_ID"], "ClientID = " + 34673)
#print DB_ID