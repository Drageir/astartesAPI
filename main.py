from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app=FastAPI()
app.title = 'AstartesAPI'
app.description = 'API de pruebas'
app.version = '0.1'

class Marine():
    id:int = None
    name:str = BaseModel(max_leght=20)
    rank:str = BaseModel(max_leght=20)
    chapter:str = BaseModel(max_leght=20)
    status:str = BaseModel(max_leght=10)

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

@app.get('/marines',tags=['Marines'])
def getMarines():
    return marines

@app.get('/marines/{id}',tags=['Marines'])
def getMarine(id:int):
    for marine in marines:
        if marine['id']==id:
            return marine
    return []

@app.get('/marines/',tags=['Marines'])
def getMarinesByStatus(name='',rank='',status='',chapter=''):
    res = []
    for marine in marines:
        if name and marine['name']!= name: continue
        if status and marine['status'] != status: continue
        if chapter and marine['chapter'] != chapter:continue
        if rank and marine['rank'] != rank: continue
        res.append(marine)
    return res

@app.post('/marine',tags=['marine'])
def createMarine(marine:Marine):
    marines.append(
        {
            'id':marine.id,
            'name':marine.name,
            'rank':marine.rank,
            'chapter':marine.chapter,
            'status':marine.status
        }
    )
    return movies

@app.put('/marine',tags=['marine'])
def actualizaMarine(id,marine:Marine):
    for marine in marines:
        if marine['id']==id:
            marine['name']=marine.name
            marine['rank']=marine.rank
            marine['chapter']=marine.chapter
            marine['status']=marine.status
            break

@app.delete('/marine/{id}',tags=['marine'])
def deleteMarine(id:int):

    for marine in marines:
        if marine['id']==id:
            marines.remove(marine)
            break
