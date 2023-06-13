import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.username = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.port = os.getenv('DB_PORT')
        self.dbname = os.getenv('DB_NAME')
        self.conn = None

    def connect(self):
        """Connect to Postgres database."""

        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as e:
                print('ERROR')
                raise e
            finally:
                print('Connection opened successfully')

    def add_rows(self, ticker, price):
        """Add rows to table."""
        self.connect()

        with self.conn.cursor() as cur:
            currency = [(ticker, price), (ticker, price)]
            cur.executemany("INSERT INTO derbit (ticker, price) VALUES (%s, %s)", currency)
            self.conn.commit()

            print('Data recorded')


db = Database()
db.connect()
