## ¿Qué es una Máquina virtual?

Una máquina virtual (VM) es un programa de computadora que simula una computadora. El software de VM que usaremos en este curso es [Virtualbox](https://download.virtualbox.org/virtualbox/6.1.12/VirtualBox-6.1.12-139181-Win.exe). Cuando configuró su máquina virtual, instaló Linux en la VM, lo que convirtió a Linux ([Raspbian](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/)) en un guest OS(Sistema operativo invitado). El sistema operativo (SO) que está instalado directamente en su computadora física (PE: Windows) se llama host OS.

## ¿Cómo se diferencia la Interfaz de línea de comandos (CLI) vs Shell ?

-	Cualquier interfaz donde ingresas lo comandos, se ejecuta y se obtiene un resultado, algunos ejemplos:

    Interfaz de línea comandos de Linux o MobaXterm.
    
    Interfaz de línea de comandos de python: python, python3
    
    
-	El programa que procesa la información escrita en el CLI es el Shell, en Linux el Shell por defecto es bash,  sin embargo se puede usar otro Shell o el intérprete de python.

## ¿Como se diferencia el Shell de una función en python?

-	Un comando del shell es una operación que ejecuta el SO. La mayoría de estos comandos ejecutan programas.
-	La función es una operación ejecutada por el sistema operativo, pero primero es interpretada por el lenguaje (Python u otro).
-	Las funciones son utilizadas para organizar un programa mientras que los comando en el Shell son utilizados para ejecutar programas.

## Algunos comandos:

- [Link 1](https://courses.cs.washington.edu/courses/cse390a/14au/bash.html)
- [Link 2](https://www.loggly.com/wp-content/uploads/2015/05/Linux-Cheat-Sheet-Sponsored-By-Loggly.pdf)

### Archivos y carpetas

#### Moverse entre carpetas:
```
cd
```
¿que son rutas relativas vs rutas absolutas?

#### Observar lo que hay dentro de una carpeta:
```
ls
```
#### Editar un archivo:

```
nano
```
#### Imprimir lo que contiene un archivo:
```
cat
```
#### Eliminar y crear una carpeta
```
rm
mk
```

### Descargas y gestor de paquetes

##### Actualizar lista de paquetes
```
apt-get update
```

##### Descargar paquetes
```
apt-get upgrade:
```

##### Instalar paquetes o programas:
```
apt-get install
```

Ejemplo de instalación y ejecución:

```
apt-get install cowsay
cd /usr/games
./cowsay
```
#### información de comandos

```
man cowsay
```

#### Descargar archivos:
```
wget
curl
```
### Iniciar python
```
python 
python3
```
Ver historial de comandos:
```
history
```
- Usar ctl+r

- Autocompletar con  tab:

#### Descargar con el gestor de paquetes de python:
```
pip
python3 -m pip
```

## Instalando un servidor WEB, el broker MQTT y el Dashboard

**Instalando Node-RED**

- ***Instalando la última version de node.js***

  ``` sudo apt-get install nodejs ```

- ***Instalando npm***

  ```sudo apt-get install npm ```

- ***Instalando Node-RED con npm***
 
  ```sudo npm install -g --unsafe-perm node-red```

- ***Inicializando el servicio Node-RED***
  
  ```sudo node-red ```

El servidor se inicia ejecutandose a traves del puerto 1880.
Para entrar al dashboard ingrese la url *ip_servidor*:1880/ o localhost:1880/ en el navegador.

**Instalando el broker Aedes y el Dashboard**

  - ***Utilizando la interfaz gráfica (GUI) de Node Red:***

  ![alt text](https://github.com/joagovi/Garbage-Classification-for-safety/blob/master/pictures/menu_node.png "menu node-red")

1. Ingresar al menu principal de node-red.
2. Seleccionar "Manage palette".
3. Seleccionar "Install".
4. Ingresar **"node-red-dashboard"** en el campo de busqueda.
5. Click en el boton **"install"**.
6. Cuando la instalación finalice, hacer click en "Done."
7. Presione F5 para recargar.
8. Encontrará el boton **"Dashboard"** a la derecha.

- **De forma similar instalar el nodo del broker Aedes: “node-red-contrib-aedes”**

**Inicializar Node-RED con un archivo pre-existente**

  1. Usar la carpeta **.node-red**: ``` cd <PATH>/.node-red/ ```
Donde .node-red es la carpeta que contiene los archivos de la aplicación.

  2. Inicializar Node-RED con el archivo que contien el flujo de datos:```sudo node-red flows_ip-172-31-87-186.json```

**Configurando los flujos de datos de node-red**

- ***Inicializar el Broker***

  Seleccionar cualquiera de los subscriptores y entonces editar el servidor con el ip de localhost. Reemplazar 52.90.89.156 por 127.0.0.1.

  ![alt text](https://github.com/joagovi/Garbage-Classification-for-safety/blob/master/pictures/edit_broker.png "select broker")

  ![alt text](https://github.com/joagovi/Garbage-Classification-for-safety/blob/master/pictures/edit_broker_2.png "edit broker")

