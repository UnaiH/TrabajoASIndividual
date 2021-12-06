FROM python:3.8-alpine3.13
WORKDIR /programa
ADD crearColas.py /programa
ADD enviar.py /programa
ADD main.py /programa
COPY requirements.txt /programa
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "main.py" ]
