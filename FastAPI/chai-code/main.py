from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas: List[Tea] = []

@app.get("/")
def root():
    return {"message" : "Hy From Home Page..!"}

@app.get("/tea_store")
def tea_store():
    return {"message" : "Hy From Tea Store..!"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int,updatedTea: Tea):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updatedTea
            return updatedTea
    return {"message" : "Error in Updating Tea."}    
    
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            removed_tea = teas.pop(index)
            return removed_tea
    return {"message" : "Error in Deleting Tea."}    