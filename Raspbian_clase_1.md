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


