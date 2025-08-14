from fastapi import FastAPI, Path


app = FastAPI()

inventory = {
    1: {
        "name" : "Milk",
        "price" : 9,
        "brand" : "Regular"
    }
}

@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int = Path(description="The ID of the Item you want to view.")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_by_name(name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"Data" : "Not found"}

