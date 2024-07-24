from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    Integer,
    DateTime,
    String,
   
    Text,
    func,
    text,
)
from src.db.config import meta, conn



makes = Table(
    "makes",
    meta,
    Column("id_make", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("img_url", Text(), nullable=False),
    Column("date", DateTime(), nullable=False, server_default=func.now())
)



meta.create_all(conn)
