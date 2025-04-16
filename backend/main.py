from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root path
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Example of another route
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
