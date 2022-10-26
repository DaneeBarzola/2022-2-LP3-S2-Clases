# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:40:25 2022

@author: Danee Jhajaira
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db") 
cursor = conexion.cursor()
consulta= """ UPDATE EDITORIAL
            SET 
                NOMBRE ='Imprenta Unión'
            WHERE
                IDEDITORIAL = 1
            """
cursor=conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()