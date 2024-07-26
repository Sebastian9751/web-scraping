import asyncio
from fastapi import APIRouter
from src.controller import motorcycle as ct

motorcycle = APIRouter(tags=["motorcycle"], prefix="/mt")

@motorcycle.get("/")
async def findData():
    
    return await ct.findAll()
     
