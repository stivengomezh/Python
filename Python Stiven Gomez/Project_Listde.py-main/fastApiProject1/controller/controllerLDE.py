from fastapi import APIRouter
from model import modelLDE
from service import serviceLDE

listde_router = APIRouter(
    prefix="/listde"
)

serviceLDE= serviceLDE.ListDEService()

@listde_router.get("/")
async def get_kids_list():
    return serviceLDE.get_kids().listKids()


@listde_router.post("/")
async def addKidToFinal(data : modelLDE.Kid):
    serviceLDE.get_kids().addKidToFinal(data)
    return {"code":200, "message": "Adicionado correctamente"}

@listde_router.post("/tostart")
async def addKidToStart(data : modelLDE.Kid):
    serviceLDE.get_kids().addKidToStart(data)
    return {"code":200, "message": "Adicionado correctamente"}

@listde_router.post("/inposition/{position}")
async def addKidInPosition(data : modelLDE.Kid, position: int ):
    serviceLDE.get_kids().addKidInPosition(data,position)
    return {"code":200, "message": "Adicionado correctamente"}

@listde_router.get("/invest")
async def investKids():
    serviceLDE.get_kids().investKids()
    return {"code":200, "message": "Invertido correctamente"}

@listde_router.post("/deleteID/{id}")
async def deleteForID(id: int ):
    serviceLDE.get_kids().deleteForID(id)
    return {"code":200, "message": "Eliminado correctamente"}

@listde_router.post("/deletePosition/{position}")
async def deleteForPosition(position: int ):
    serviceLDE.get_kids().deleteForPosition(position)
    return {"code":200, "message": "Eliminado correctamente"}
@listde_router.get("/interleaveGender")
async def interleaveByGender():
    serviceLDE.get_kids().interleaveByGender()
    return {"code":200, "message": "Intercalado correctamente"}
@listde_router.get("/interleaveHeadAndTail")
async def interleaveHeadAndTail():
    serviceLDE.get_kids().interleaveHeadAndTail()
    return {"code":200, "message": "Intercalado correctamente"}