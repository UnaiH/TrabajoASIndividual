#!/usr/bin/env python
import pika
import sys

print("Creando colas")

conexion= pika.BlockingConnection(pika.ConnectionParameters(host = 'rabbitmq', port = 5672, credentials= pika.PlainCredentials('usuario', '123456')))
canal=conexion.channel()

canal.queue_declare(queue='Importante')
canal.queue_declare(queue='Aviso')
canal.queue_declare(queue='MensajeInterno')

print("Colas: Importante, Aviso y MensajeInterno creadas")
conexion.close()
