from ..connect import Connect


class User(Connect):

    def __init__(self) -> None:
        super().__init__()

    def create(self, **kwargs):
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `users` ({}) VALUES ({})"
                columns = ', '.join(kwargs.keys())
                placeholders = ', '.join(['%s'] * len(kwargs))
                sql = sql.format(columns, placeholders)

                cursor.execute(sql, tuple(kwargs.values()))
                self.connection.commit()

        return kwargs

    def get_all(self) -> list:
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM `users`
                """)

        return cursor.fetchall()