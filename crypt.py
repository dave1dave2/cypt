# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet
import pymysql
import csv

#se connecter à la base de donnée
connection = pymysql.connect(user='dave', host='localhost', password='dave')
cur = connection.cursor()

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

#cette fonction est utilisé pour charger la clé de cryptage
def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()
#load_key()

#definissons une fonction pour ajouter une table à la base de donnée
def crypt():
    cur = connection.cursor()
    cur.execute("use dave")
    cur.execute("select email from client where id = 1 ")
    rows = cur.fetchone()
    
    for a in rows :
        key = load_key()
        encoded_message = a.encode()
        f = Fernet(key)
        B = f.encrypt(encoded_message)
        C = B.decode()
        cur.execute("update client set email =%s where id = 1",(C))
        connection.commit()

    #ligne 2
    cur.execute("select email from client where id = 2 ")
    rows = cur.fetchone()
    
    for a in rows :
        key = load_key()
        encoded_message = a.encode()
        f = Fernet(key)
        B = f.encrypt(encoded_message)
        C = B.decode()
        cur.execute("update client set email =%s where id = 2",(C))
        connection.commit()

    #ligne3
    cur.execute("select email from client where id = 3 ")
    rows = cur.fetchone()
    
    for a in rows :
        key = load_key()
        encoded_message = a.encode()
        f = Fernet(key)
        B = f.encrypt(encoded_message)
        C = B.decode()
        cur.execute("update client set email =%s where id = 3",(C))
        connection.commit()


crypt()
