## Instalando Kivy

Esta guia se ha realizado en base a los siguientes link:

[link 1](https://kivy.readthedocs.io/en/master/installation/installation-rpi.html)

[link 2](https://kivy.org/doc/stable/installation/installation-linux.html)

Para levantar Kivy de la consola se necesita compilar SDL2 desde codigo, esto trabaja bajo X11.

Instalar los requerimientos:

```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install libfreetype6-dev libgl1-mesa-dev libgles2-mesa-dev libdrm-dev libgbm-dev libudev-dev libasound2-dev liblzma-dev libjpeg-dev libtiff-dev libwebp-dev git build-essential
sudo apt-get install gir1.2-ibus-1.0 libdbus-1-dev libegl1-mesa-dev libibus-1.0-5 libibus-1.0-dev libice-dev libsm-dev libsndio-dev libwayland-bin libwayland-dev libxi-dev libxinerama-dev libxkbcommon-dev libxrandr-dev libxss-dev libxt-dev libxv-dev x11proto-randr-dev x11proto-scrnsaver-dev x11proto-video-dev x11proto-xinerama-dev
```

Instalar SDL2:

```
wget https://libsdl.org/release/SDL2-2.0.10.tar.gz
tar -zxvf SDL2-2.0.10.tar.gz
pushd SDL2-2.0.10
./configure --enable-video-kmsdrm --disable-video-opengl --disable-video-x11 --disable-video-rpi
make -j$(nproc)
sudo make install
popd
```

Instalar SDL2_image:

```
wget https://libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz
tar -zxvf SDL2_image-2.0.5.tar.gz
pushd SDL2_image-2.0.5
./configure
make -j$(nproc)
sudo make install
popd
```

Instalar SDL2_mixer:

```
wget https://libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz
tar -zxvf SDL2_mixer-2.0.4.tar.gz
pushd SDL2_mixer-2.0.4
./configure
make -j$(nproc)
sudo make install
popd
```

Instalar SDL2_ttf:

```
wget https://libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz
tar -zxvf SDL2_ttf-2.0.15.tar.gz
pushd SDL2_ttf-2.0.15
./configure
make -j$(nproc)
sudo make install
popd
```

**Instalar las dependencias:**

```
sudo apt update
sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python3-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python3-dev libmtdev-dev \
   xclip xsel libjpeg-dev
```

**Instalar las dependencias de pip:**

```
python3 -m pip install --upgrade --user pip setuptools
python3 -m pip install --upgrade --user Cython==0.29.19 pillow
```

**Instalando el paquete kivy (master)**

***Finalmente compilar e instalar Kivy (master) y opcionalmente los ejemplos (kivy-examples):***

```
python3 -m pip install --user https://github.com/kivy/kivy/archive/master.zip
python3 -m pip install kivy_examples
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


