from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.router.motorcycle import motorcycle

app = FastAPI(
    title="MY-API",
    description="This API is awesome.",
)

#Routes
app.include_router(motorcycle)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def helloworld():
    
    
    
    
    return "Hello world"
