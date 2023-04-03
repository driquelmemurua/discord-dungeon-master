# discord-dungeon-master

## VENV

Abre una terminal y navega hasta el directorio de tu proyecto.

Ejecuta el siguiente comando para crear un ambiente virtual:

`python3 -m venv venv`

Este comando creará un directorio llamado **venv** en tu proyecto que contiene todos los archivos necesarios para crear un ambiente virtual.

Activa el ambiente virtual con el siguiente comando:

`source venv/bin/activate`

Este comando activa el ambiente virtual venv y ahora todos los paquetes de Python que instales serán instalados en este ambiente virtual.

Ahora puedes instalar las dependencias del proyecto utilizando el siguiente comando:

`pip install -r requirements.txt`

Cuando hayas terminado de trabajar en tu proyecto, puedes desactivar el ambiente virtual ejecutando el siguiente comando:

`deactivate`

Esto desactivará el ambiente virtual **venv** y volverás al ambiente de Python global.

Con el archivo requirements.txt, otras personas que quieran trabajar en tu proyecto pueden crear su propio ambiente virtual y ejecutar el siguiente comando para instalar todas las dependencias:

Para correr el proyecto ejecutar el comando:

`python main.py`

Puedes invitar al bot a tu servidor con el siguiente [enlace](https://discord.com/api/oauth2/authorize?client_id=1092247272361828373&permissions=3072&scope=bot).
