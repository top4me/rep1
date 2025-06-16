[app]

# Настройки приложения
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# Требования
requirements = python3, kivy==2.3.0, android

# Android SDK
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_path = 

# Разрешения
android.permissions = INTERNET

# Иконки и ассеты
icon.filename = icon.png
presplash.filename = presplash.png
orientation = portrait
fullscreen = 0

# Настройки сборки
android.arch = arm64-v8