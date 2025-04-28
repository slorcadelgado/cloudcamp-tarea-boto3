# cloudcamp-tarea-boto3

- **Instalar AWS cli**
- **Instalar jq y curl en el sistema operativo**
- **Con el siguiente comando como base: aws ec2 describe-security-groups |jq .SecurityGroups[].GroupId**
- **Hacer la averiguación de lo que hace el comando (explicarlo y subir un readme en el repositorio)**
- **Escribir un archivo python que realice la misma funcion**

# Comando `aws ec2 describe-security-groups |jq .SecurityGroups[].GroupId`

- **aws ec2 describe-security-groups:** Lista todos los Security Groups de una cuenta en una región específica, en este caso us-east-1.
- **|:** El pipe pasa la salida de ese comando al siguiente programa.
- **jq .SecurityGroups[].GroupId:** Usa jq (una herramienta para procesar JSON) para extraer el campo GroupId de cada elemento dentro del arreglo SecurityGroups.

**En resumen, el comando lista los IDs de todos los Security Groups de una cuenta en una región, en este caso us-east-1 porque es la región que se configuró previamente con el comando aws configure.**

# ¿Cómo ejecutar el programa?

1. **Crear venv:** `python3 -m venv .venv`
2. **Instalar dependencias:** `.venv/bin/pip install -r requirements.txt`
3. **Ejecutar el programa:** `.venv/bin/python3 sg.py`