#!/usr/bin/env python
#Se importan las librerias necesarias
import pika
import sys
print("Creando colas")
#Se inicializa la variable conexion con el objeto BlockingConnection de la libreria pika con los parametros necesarios
conexion= pika.BlockingConnection(pika.ConnectionParameters(host = 'rabbitmq', port = 5672, credentials= pika.PlainCredentials('usuario', '123456')))
#Se inicializa la variable calnal con el channel de la conexion
canal=conexion.channel()
#Se crean las tres colas con los nombres Importante, Aviso, MensajeInterno
canal.queue_declare(queue='Importante')
canal.queue_declare(queue='Aviso')
canal.queue_declare(queue='MensajeInterno')

print("Colas: Importante, Aviso y MensajeInterno creadas")
#Se cierra la conexion
conexion.close()
