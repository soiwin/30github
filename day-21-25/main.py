from fastapi import FastAPI

from routers import router


app = FastAPI(title='Bamboo Cargo')

app.include_router(router)
