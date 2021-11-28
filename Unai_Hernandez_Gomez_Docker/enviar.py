#!/usr/bin/env python
import pika
import sys
import subprocess
print("Comienzo del enviado de mensaje")
conexion= pika.BlockingConnection(pika.ConnectionParameters(host = 'rabbitmq', port = 5672, credentials= pika.PlainCredentials('usuario', '123456')))
canal=conexion.channel()

mensaje= "Hola Mundo"
cola= "Importante"
canal.basic_publish(exchange='', routing_key=cola, body=mensaje)
print("Enviado", mensaje, "a la cola", cola)
conexion.close()
print("Si se desean ver las conexiones realizadas se pueden observar poniendo en el navegador 127.0.0.1:15672")
