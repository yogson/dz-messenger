from os import environ

SERVER_HOST = environ.get("SERVER_HOST", "localhost")
SERVER_PORT = int(environ.get("SERVER_PORT", 8765))

DATABASE_URL = environ.get("DATABASE_URL")

try:
    from local_settings import *
except ImportError:
    pass
