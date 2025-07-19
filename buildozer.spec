[app]

# Título de la aplicación
title = ControlVencimientos

# Configuración del paquete
package.name = controlvencimientos
package.domain = org.tudominio

# Directorios y versión
source.dir = .
version = 0.1

# Requerimientos (ajustados para compatibilidad)
requirements = python3,kivy==2.3.0,cython==0.29.36

# Configuración específica para Android
android.arch = arm64-v8a
android.sdk_path = ./cmdline-tools
android.ndk_path = /home/runner/android-tools/android-ndk
android.ndk_version = 25b
android.sdk = 34
android.minapi = 21
android.targetapi = 34
android.gradle_download = True
android.accept_sdk_license = True

# Permisos (ajusta según necesites)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Opciones de build
android.release_artifact = .apk
p4a.branch = master
android.wakelock = True

# Configuración de log
log_level = 2

[buildozer]
# Configuración para GitHub Actions
log_level = 2
warn_on_root = 1
