from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()


db_host = os.getenv("DB_HOST", "localhost")
db_port = int(os.getenv("DB_PORT", "5432"))
db_user = os.getenv("DB_USER", "root")
db_password = os.getenv("DB_PASSWORD", "root")
db_name = os.getenv("DB_NAME", "mydb")

try:
    db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_url, echo=False)
    conn = engine.connect()
    meta = MetaData()
    print("*** successful connection ***")

except SQLAlchemyError as ex:
    print("Connection error: {}".format(ex))
