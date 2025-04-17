import json, os
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

FILE = "emotions.json"
router = APIRouter()

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

class Item(BaseModel):
    rating: int
    note: str

@router.get("/emotions")
def get_items():
    return load_data()

@router.post("/emotions")
def add_item(item: Item):
    data = load_data()
    entry = item.dict()
    entry["timestamp"] = datetime.now().isoformat()
    data.append(entry)
    save_data(data)
    return {"message": "Added", "data": entry}
