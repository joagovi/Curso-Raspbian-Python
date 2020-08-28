## Instalando Kivy

Esta guia se ha realizado en base a los siguientes link:

[link 1](https://kivy.readthedocs.io/en/master/installation/installation-rpi.html)

[link 2](https://kivy.org/doc/stable/installation/installation-linux.html)

Para levantar Kivy de la consola se necesita compilar SDL2 desde codigo, esto trabaja bajo X11.

**Instalar las dependencias:**

```
sudo apt update
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python3-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python3-dev libmtdev-dev \
   xclip xsel libjpeg-dev
```

**Instalar DL2:**

```
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

**Instalar las dependencias de pip:**

```
python3 -m pip install --upgrade --user pip setuptools
python3 -m pip install --upgrade --user Cython==0.29.19 pillow
```

**Instalando el paquete kivy (master)**

***Instalar wheel ***

```
python3 -m pip install --upgrade --user wheel
```

***Finalmente compilar e instalar Kivy (wheels) y opcionalmente los ejemplos (kivy-examples):***

```
python -m pip install kivy
python -m pip install kivy_examples
```

***Moverse a la carpeta de instalación de los ejemplos y ejecutar el main.py***

```
cd /usr/local/share/kivy-examples/demo/showcase
```
***Instalar Garden***

```
python3 -m pip install kivy-garden
garden install graph
```


