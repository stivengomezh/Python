from fastapi import APIRouter
from model import modelLSE
from service import serviceLSE

listse_router = APIRouter(
    prefix="/listse"
)

serviceLSE= serviceLSE.ListSEService()

@listse_router.get("/")
async def get_kids_list():
    return serviceLSE.get_kids().get_head()


@listse_router.post("/")
async def addKidToFinal(data : modelLSE.Kid):
    serviceLSE.get_kids().addKidToFinal(data)
    return {"code":200, "message": "Adicionado correctamente"}
@listse_router.post("/tostart")
async def addKidToStart(data : modelLSE.Kid):
    serviceLSE.get_kids().addKidToStart(data)
    return {"code":200, "message": "Adicionado correctamente"}

@listse_router.post("/inposition/{position}")
async def addKidInPosition(data : modelLSE.Kid, position: int ):
    serviceLSE.get_kids().addKidInPosition(data,position)
    return {"code":200, "message": "Adicionado correctamente"}

@listse_router.get("/invest")
async def investKids():
    serviceLSE.get_kids().investKids()
    return {"code":200, "message": "Invertido correctamente"}
@listse_router.post("/deleteID/{id}")
async def deleteForID(id: int ):
    serviceLSE.get_kids().deleteForID(id)
    return {"code":200, "message": "Eliminado correctamente"}
@listse_router.post("/deletePosition/{position}")
async def deleteForPosition(position: int ):
    serviceLSE.get_kids().deleteForPosition(position)
    return {"code":200, "message": "Eliminado correctamente"}
@listse_router.get("/interleaveGender")
async def interleaveByGender():
    serviceLSE.get_kids().interleaveByGender()
    return {"code":200, "message": "Intercalado correctamente"}
@listse_router.get("/interleaveHeadAndTail")
async def interleaveHeadAndTail():
    serviceLSE.get_kids().interleaveHeadAndTail()
    return {"code":200, "message": "Intercalado correctamente"}