[app]
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
requirements = python3, kivy==2.3.0, android  # Убраны лишние пробелы

# Жёстко фиксируем версии SDK/NDK
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34  # Исправлено на актуальную версию
android.ndk_path = /path/to/ndk  # Если нужно

# Указываем явный путь для APK
android.release_artifact = bin/{title}-{version}-debug.apk

# Оптимизация
android.arch = arm64-v8a  # Собираем только для одной архитектуры