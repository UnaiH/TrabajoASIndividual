#!/usr/bin/env python
#Se importan las librerias necesarias
import pika
import sys
import subprocess
print("Comienzo del enviado de mensaje")
#Se inicializa la variable conexion con los parametros necesarios a partir del metodo BlockingConnection de la libreia pika
conexion= pika.BlockingConnection(pika.ConnectionParameters(host = 'rabbitmq', port = 5672, credentials= pika.PlainCredentials('usuario', '123456')))
#Se inicializa la variable canal con el channel de la conexion
canal=conexion.channel()
#Se inicialian las variables mensaje y cola
mensaje= "Hola Mundo"
cola= "Importante"
#Se publica el mensaje en la cola indicada con el exchange predefinido
canal.basic_publish(exchange='', routing_key=cola, body=mensaje)
print("Enviado", mensaje, "a la cola", cola)
#Se cierra la conexion
conexion.close()
print("Si se desean ver las conexiones realizadas se pueden observar poniendo en el navegador 127.0.0.1:15672")
