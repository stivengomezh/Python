from fastapi import FastAPI
from controller import controllerLSE
from controller import controllerLDE

app = FastAPI()

app.include_router(controllerLSE.listse_router)
app.include_router(controllerLDE.listde_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}