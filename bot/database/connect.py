import json

from pymysql import connect
from pymysql.cursors import DictCursor


class Connect:

    def __init__(self) -> None:
        config = self.load_config()

        self.connection = connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["table"],
            cursorclass=DictCursor
        )

    def load_config(self) -> dict:
        try:
            with open("config/database.json", "r") as file:
                result = json.loads(file.read())
        except FileExistsError:
            return None
        else:
            return result