# discord-dungeon-master

## Instalación

Para correr el proyecto necesitas tener instalado [Python](https://www.python.org).

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

## Variables de ambiente

Debes copiar el archivo ".env.example" y crear tu propio archivo ".env" dentro del mismo directorio:

- DISCORD_BOT_TOKEN: El token de tu aplicación de Discord, para más información puedes leer la [documentación de Discord](https://discord.com/developers/docs/getting-started#adding-credentials).

## Iniciar

Para iniciar el proyecto se puede ejecutar el comando:

`python main.py`

Para invitar al bot al servidor puedes ingresar al siguiente [enlace](https://discord.com/api/oauth2/authorize?client_id=1092247272361828373&permissions=3072&scope=bot). Para más información acerca crear un bot de Discord e invitarlo a tu servidor puedes leer la [documentación](https://discord.com/developers/docs/getting-started#step-1-creating-an-app).

## Comandos

### Estado
Puedes consultar por un estado alterado escribiendo el siguiente mensaje en cualquier canal:

`
!estado "Estado"
`

El estado puede ser uno de la siguiente lista:
- blinded
- charmed
- deafened
- exhaustion
- frightened
- grappled
- incapacitated
- invisible
- paralyzed
- petrified
- poisoned
- prone
- restrained
- stunned
- unconscious
