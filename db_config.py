import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")


def load_db_config():
    parser = configparser.ConfigParser()
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(
            f"Не найден файл конфигурации {CONFIG_PATH}. "
            "Скопируйте config.ini.example в config.ini и укажите параметры подключения."
        )
    parser.read(CONFIG_PATH, encoding="utf-8")
    section = parser["database"]
    return {
        "host": section.get("host", "localhost"),
        "port": section.getint("port", fallback=5432),
        "database": section.get("database", ""),
        "user": section.get("user", ""),
        "password": section.get("password", ""),
    }


DB_CONFIG = load_db_config()
