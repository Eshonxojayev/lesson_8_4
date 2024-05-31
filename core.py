from fastapi import FastAPI
from auth import auth_router
from category import category_router
from orders import order_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(order_router)

@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }

@app.get("/user")
async def intro():
    return {
        "message": "user page"
    }

@app.get("/user/{id}")
async def intro(id: int):
    return {
        "message": f"user - {id}"
    }

@app.post("/user")
async def intro():
    return {
        "message": "This is post request"
    }



@app.get("/test2")
async def test2():
    return {
        "message": "This is test page"
    }