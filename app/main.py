<<<<<<< HEAD
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router as router_api

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')

=======
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router as router_api

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')

>>>>>>> amvera/master
app.include_router(router_api)