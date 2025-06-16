[app]

# Название приложения
title = My Kivy App

# Имя пакета (должно быть уникальным)
package.name = myapp

# Домен (обычно перевернутый домен разработчика)
package.domain = org.test

# Путь к основной Python-логике
source.dir = .

# Главный файл приложения
source.include_exts = py,png,jpg,kv,atlas,ttf

# Версия приложения (format: major.minor.revision)
version = 0.1

# Требуемая версия Kivy
requirements = python3,kivy==2.3.0,android

# Укажите версию SDK и NDK (можно оставить по умолчанию)
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 24

# Разрешения для Android (указывайте только необходимые)
android.permissions = INTERNET

# Ориентация экрана (portrait или landscape)
orientation = portrait

# Иконка (убедитесь, что файл существует)
icon.filename = icon.png

# Логотип запуска (presplash)
presplash.filename = presplash.png

# Дополнительные настройки
fullscreen = 0
android.accept_sdk_license = True

# (Опционально) Укажите дополнительные зависимости
# requirements = kivy, openssl, requests, pillow

# (Опционально) Настройки для release-сборки
# key.keystore = 
# key.alias = 
# key.store_password = 
# key.alias_password = 