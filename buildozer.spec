[app]

# (str) Título de tu aplicación
title = ControlVencimientos

# (str) Nombre del paquete
package.name = controlvencimientos

# (str) Dominio del paquete (org.test, com.miempresa, etc.)
package.domain = org.tudominio

# (str) Carpeta donde está tu código fuente principal
source.dir = .

# (list) Extensiones de archivos fuente a incluir
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json

# (list) Lista de requerimientos en formato pip
requirements = python3,kivy==2.3.0,cython==0.29.36

# (str) Versión de la app
version = 0.1

# (list) Permisos de Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Nivel mínimo de API
android.minapi = 21

# (int) Nivel objetivo de API
android.targetapi = 34

# (list) Arquitecturas a compilar
android.archs = arm64-v8a

# (bool) Aceptar licencias SDK automáticamente
android.accept_sdk_license = True

# (bool) Descargar Gradle si hace falta
android.gradle_download = True

# (str) Rama de python-for-android a usar
p4a.branch = master

# (bool) Mantener la pantalla encendida
android.wakelock = True

# (str) Tipo de artefacto a generar: 'apk' o 'aab'
android.release_artifact = apk

# (list) Patrones de archivos/directorios a excluir del APK
#android.exclude_patterns =

# (str) Presplash (pantalla de carga)
#android.presplash_color = #FFFFFF

# (str) Icono de la app
#android.icon = icon.png

# ------------------------------------------------------------------
[buildozer]

# (int) Nivel de log: 1=error, 2=warning, 3=info, 4=debug
log_level = 2

# (bool) Advertir si se ejecuta como root
warn_on_root = 1

# (int) Número de procesos de compilación paralelos
#buildozer.build_processes = 4
