import json
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


note=APIRouter()
templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request): 
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"]
        })
    return templates.TemplateResponse ("index.html",{"request":request,"newDocs":newDocs}) 

@note.post("/",response_class=HTMLResponse)
async def create_item(request:Request):
    # print notes
    form = await request.form()
    formDict=dict(form)
    # print(type(form))
    # for key,value in form.items():
    #     formDict[key]=value
    #    send notes to database
    if(formDict["important"] == "on"):
        formDict["important"]=True # type: ignore
    else:
        formDict["important"]=False # type: ignore
         
    print("formDict",type(formDict),formDict)
    
    note =conn.notes.notes.insert_one(formDict) 
    # retrive to show
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"]
        })
    return templates.TemplateResponse ("index.html",{"request":request,"newDocs":newDocs})
    

