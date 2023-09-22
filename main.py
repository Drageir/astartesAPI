from fastapi import FastAPI, Body,Path
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List


app=FastAPI()
app.title = 'AstartesAPI'
app.description = 'API de pruebas'
app.version = '0.1'

class Marine(BaseModel):
    id: Optional[int] = None
    name:str = Field(max_leght=20)
    rank:str = Field(max_leght=20)
    chapter:str = Field(max_leght=20)
    status:str = Field(max_leght=10)


marines = [
    {
        'id':1,
        'name':"Saul Tarvitz",
        'rank': 'captain',
        'chapter': "Emperor's Children",
        'status':'kia'
    },
    {
        'id':2,
        'name':"Garviel Loken",
        'rank': 'captain',
        'chapter': 'Luna Wolves',
        'status':'kia'
    },
    {
        'id':3,
        'name':"Dante",
        'rank': 'chapter master',
        'chapter': 'Blood Angels',
        'status':'active'
    },
    {
        'id':4,
        'name':"Sanguinius",
        'rank': 'primarc',
        'chapter': 'Blood Angels',
        'status':'kia'
    }
]



@app.get('/',tags=['Home'])
def mensaje():
    return HTMLResponse('<h1>Buenos días</h1>')

@app.get('/marines',tags=['Marines'],response_model=List[Marine])
def getMarines() -> List[Marine]:
    return JSONResponse(content = marines)

@app.get('/marines/{id}',tags=['Marines'],response_model=Marine)
def getMarine(id:int = Path(ge=1,le=2000)) -> Marine:
    for marine in marines:
        if marine['id']==id:
            return JSONResponse(content = marine)
    return JSONResponse(content = [])

@app.get('/marines/',tags=['Marines'],response_model=List[Marine])
def getMarinesByStatus(name='',rank='',status='',chapter='') -> List[Marine]:
    res = []
    for marine in marines:
        if name and marine['name']!= name: continue
        if status and marine['status'] != status: continue
        if chapter and marine['chapter'] != chapter:continue
        if rank and marine['rank'] != rank: continue
        res.append(marine)
    return JSONResponse(content = res)

@app.post('/marine',tags=['marine'],response_model=dict)
def createMarine(marine:Marine) -> dict:
    for m in marines:
        if m['id'] > marine.id: break
        if m['id'] == marine.id:
            return JSONResponse(content = {"message":"Error. El registro ya existe"})
    marines.append(marine)
    return JSONResponse(content = "Se ha registrado el marine correctamente")

@app.put('/marine',tags=['marine'],response_model=dict)
def actualizaMarine(marine:Marine)-> dict:
    for m in marines:
        if m['id']==marine.id:
            m['name']=marine.name
            m['rank']=marine.rank
            m['chapter']=marine.chapter
            m['status']=marine.status
            break

@app.delete('/marine/{id}',tags=['marine'], response_model = dict)
def deleteMarine(id:int) -> dict:

    for marine in marines:
        if marine['id']==id:
            marines.remove(marine)
            break
