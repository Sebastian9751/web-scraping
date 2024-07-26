import pandas as pd
from src.db.config import conn
from src.model.make import makes
from src.driver.index import Driver


async def findAll():

    driver = Driver()

    # data = conn.execute(makes.select())
    # df = pd.DataFrame(data, columns=makes.c.keys())

    return driver.get_data()
