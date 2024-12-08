from tinydb import TinyDB

from app.internal.validation import Validation
from app.lib.config import config


db = TinyDB(config["db_path"])
