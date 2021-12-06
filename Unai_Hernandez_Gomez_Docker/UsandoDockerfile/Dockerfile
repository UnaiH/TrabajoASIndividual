#Imagen base
FROM python:3.8-alpine3.13
#Se crea un directorio llamado programa
WORKDIR /programa
#Se añaden los archivos python del cliente que son crearColas.py, enviar.py y main.py
ADD crearColas.py /programa
ADD enviar.py /programa
ADD main.py /programa
#Se copia el requirements.txt en el directorio programa
COPY requirements.txt /programa
#Se actualizan las librerias
RUN pip3 install --upgrade pip
#Se instalan las librerias especificadas en el archivo requirements.txt
RUN pip3 install -r requirements.txt
#Se ejecuta en la terminal el comando para ejecutar el cliente
CMD [ "python3", "main.py" ]
