FROM ubuntu:22.04

# 1. Configuración base
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get update -o Acquire::Retries=5

# 2. Instalar Python 3.9 desde repositorio oficial (sin compilar)
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    python3-pip \
    && apt-get clean

# 3. Configurar Python 3.9 como predeterminado
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 && \
    ln -s /usr/bin/python3.9 /usr/bin/python3

# 4. Actualizar pip e instalar wheel
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install wheel

# 5. Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    zip \
    openjdk-17-jdk-headless \
    zlib1g-dev \
    libncurses5-dev \
    autoconf \
    automake \
    libtool \
    pkg-config \
    libffi-dev \
    libssl-dev \
    && apt-get clean

# 6. Instalar Kivy y dependencias gráficas
RUN apt-get install -y \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    && apt-get clean

# 7. Instalar Cython y Kivy primero
RUN python3 -m pip install --no-cache-dir cython==0.29.36 && \
    python3 -m pip install --no-cache-dir kivy==2.2.0

# 8. Instalar Buildozer sin python-for-android
RUN python3 -m pip install --no-cache-dir buildozer==1.4.0

# 9. Instalar python-for-android desde el repositorio de Kivy
RUN git clone https://github.com/kivy/python-for-android.git && \
    cd python-for-android && \
    git checkout 2022.10.05 && \
    python3 setup.py install && \
    cd .. && \
    rm -rf python-for-android

WORKDIR /app