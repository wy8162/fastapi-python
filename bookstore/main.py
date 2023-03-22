from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from bookstore.api.routes import routes


def create_app():
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(routes)
    return application


app = create_app()
