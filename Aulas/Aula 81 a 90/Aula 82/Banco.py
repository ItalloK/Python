import sqlite3
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+"\\agendatkinter.db"

def ConexaoBanco():
    conn = None
    try:
        conn = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return conn

def Dql(query): # Select
    vcon = ConexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def Dml(query): #Insert, Update, Delete
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
