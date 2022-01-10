import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# import staticfiles
from fastapi.staticfiles import StaticFiles

from config import settings

# routes importing
from apps.site import router as site_router
from apps.services import router as services_router
# from dependencies import get_api_app_client

# import database
# from database.main_db import db_provider

# include all necessary routes
app = FastAPI(
    # dependencies=[Depends(get_api_app_client)]
)
# mount static files folder
app.mount("/static", StaticFiles(directory="static"), name = "static")

# setting up app cors
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    # allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# include app routes
app.include_router(site_router.router)
app.include_router(services_router.router)


@app.on_event('startup')
async def startup_db_client():
    print('settings are', settings.dict())
    pass
    # print('db provider is', db_provider)

@app.on_event('shutdown')
async def shutdown_db_client():
    pass
    # db_provider.db_client.close()

@app.get("/status")
def get_status():
    """ Get status of server """
    return {
        "status": "running",
        # "settings": settings.dict(),
        }

# initial app run
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        reload=settings.DEBUG_MODE,
        port=8000,
    )
