[app]
title = ControlVencimientos
package.name = controlvencimientos
package.domain = org.tudominio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
version = 0.1
requirements = python3,kivy==2.3.0

android.permissions = INTERNET
android.minapi = 21
android.targetapi = 34
android.archs = arm64-v8a
android.accept_sdk_license = True
android.release_artifact = apk
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
