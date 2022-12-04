from typing import List

from fastapi import FastAPI

from app.__version import VERSION
from app.db import database
from app.roles.utils import create_default_roles
from app.scopes.models import Scope
from app.scopes.utils import create_scopes
from app.users.models import User

from fastapi_pagination import add_pagination

# Routes
from app.users.views import router as users_router
from app.auth.views import router as auth_router
from app.scopes.views import router as scopes_router
from app.roles.views import router as roles_router


def create_app():
    _app = FastAPI(
        version=VERSION,
        debug=True
    )

    _app.state.database = database
    _app.include_router(users_router, prefix="/users", tags=["users"])
    _app.include_router(auth_router, prefix="/auth", tags=["auth"])
    _app.include_router(scopes_router, prefix="/scopes", tags=["scopes"])
    _app.include_router(roles_router, prefix="/roles", tags=["roles"])
    add_pagination(_app)

    @_app.on_event("startup")
    async def startup():
        database_ = _app.state.database
        if not database_.is_connected:
            await database.connect()
        await create_scopes()
        await create_default_roles()

    @_app.on_event("shutdown")
    async def shutdown():
        database_ = _app.state.database
        if database_.is_connected:
            await database_.disconnect()

    @_app.get("/")
    async def home():
        return {}

    return _app


app = create_app()
