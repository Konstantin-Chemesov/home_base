from fastapi import FastAPI
from database import Model, engine
from routers import speedster

app = FastAPI()

# @app.get("/{item_id}")
# async def root(item_id):
#     return {"message": item_id}

Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(speedster.router)