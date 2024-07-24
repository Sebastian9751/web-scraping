import pandas as pd
from src.db.config import conn
from src.model.make import makes

async def findAll():

    data = conn.execute(makes.select())
    
    
    
    df = pd.DataFrame(data, columns=makes.c.keys(),)
    
    
    return df.to_dict(orient="records")
