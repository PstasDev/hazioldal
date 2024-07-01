
# Ez a fájl egy minta a local_settings.py fájlhoz.
# Ezt a fájlt kell átnezevni local_settings.py-re és a saját adatokkal feltölteni.
# Ebben nincs sok minta érték, csak a változók nevei, melyek sorrendje elhanyagolható.

# Hogyan tudsz saját Secret Key-t generálni?
# A következő parancsot kell futtatni a terminálban:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

SECRET_KEY = '' #ide írd a saját secret key-edet

# Állítsd False-ra, ha nem akarsz debug módban dolgozni
# Ha False-ra állítod, akkor be kell állítsd, hogy kezelje a szerver a statikus fájlokat

DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = False

# Ha 'otthon'-ra állítod, akkor a program Sqlite adatbázist használ.
# Ha 'postgresotthon'-ra állítod, akkor a program Postgres adatbázist használ.
# Ha 'DigitalOcean'-ra állítod, akkor a program Postgres adatbázist használ.
MELYIK = "otthon"

# Az adatbázis nevét a 'psql' parancs futtatásával, majd az adatbázisok listájának lekérdezésével tudod megtudni.
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "" #sajat jelszavad postgres telepítéséből
DB_HOST = "localhost"

#hagyd üresen nyugodtan, ha nincs beállítva email küldés, anélkül is működik a program
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = ""
EMAIL_USE_TLS = "" # meggyozodesem hogy boolean de mindegy
DEFAULT_FROM_EMAIL = ""