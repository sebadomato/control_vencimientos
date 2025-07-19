[app]
title = ControlVencimientos
package.name = controlvencimientos
package.domain = org.tudominio
source.dir = .
version = 0.1
requirements = python3,kivy==2.3.0,cython==0.29.36

# Android config
android.archs = arm64-v8a
android.sdk_path = ./cmdline-tools
android.ndk_path = ./android-ndk
android.minapi = 21
android.targetapi = 34
android.gradle_download = True
android.accept_sdk_license = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.release_artifact = .apk
p4a.branch = master
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1
