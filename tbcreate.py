# -*- coding: utf-8 -*-
import pymysql
import csv

#se connecter à la base de donnée
connection = pymysql.connect(user='dave', host='localhost', password='dave')
cur = connection.cursor()

#definissons une fonction pour ajouter une table à la base de donnée
def ajout():
	cur = connection.cursor()
	#cur.execute("set global local_infile = 1 ")
	#connection.commit()
	#Se connecter à la base de donnée dave
	cur.execute("use dave")
	#cur.execute('drop table personne')
	#Créer une table 
	cur.execute ("create table client (id int PRIMARY KEY, Nom VARCHAR(10),Prenom VARCHAR(15), email VARCHAR(100),numero varchar(15),compteur varchar(15))")
	# enregistrer les valeur dans la base de de bonnées 
	connection.commit()

	#importont un fichier csv dans une table 
	#repertorier le ficher à importer dans le repertoire par défaut. trouver le répertoir à partir de cette commande show variables like 'secure_file_priv' 

	cur.execute("load data  infile '/var/lib/mysql-files/clientcopie.csv' into table client fields terminated by ';' lines terminated by '\r\n' ignore 1 lines ")
	connection.commit()
	cur.execute("select * from client")
	rows1 = cur.fetchall()
	print(rows1)

ajout()