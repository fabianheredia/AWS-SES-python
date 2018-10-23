# AWS-SES-python
Proyecto que plantea un ejemplo de uso del servicio de colas AWS SES y una operación básica, esto usando python y el API de AWS

# Como funciona
se tienen dos script en python uno envia un mensaje y el otro recibe la informacion

# Como Instalar
* Crear una instancia de EC2 (puede ser una gratis)
* Actualizar repositorio ``` atp-get update ```
* se debe instalar pip ``` sudo apt install python-pip ```
* instalar Boto API AWS ``` pip install boto3 ```
* para que funcione el envio y recepcion de mensajes es necesario configurar el access key y secret key en la ruta 
```~/.aws/credentials``` es necesaario incluir:

``` 
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
``` 
en la siguiente ruta ``` ~/.aws/config```
``` 
[default]
region=us-east-1 
```
> para tener las llaves de acceso, es necesario ir al servicio IAM en la pestaña de usuarios en la opcion de credenciales de seguridad.

# Como hacer que funcione
## envio de mensajes
- entre al servicio de SQS y cree una secuencia de colas, coloquele un nombre y en la definicion de este recuerde la url del servicio.
- en una instancia EC2, use la siguiente sentencia:
```python3 principal.py ```
## lectura y eliminacion de mensajes
- en una instancia EC2, use la siguiente sentencia:
```python3 segundo.py ```



