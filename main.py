from fastapi import FastAPI


app = FastAPI()

inventory = {
    1: {
        "name" : "Milk",
        "price" : 9,
        "brand" : "Regular",
    }
}

@app.get('/get-item/{item_id}')
def get_item(item_id: int):

