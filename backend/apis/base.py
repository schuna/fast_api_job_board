from fastapi import APIRouter
from apis.version1 import route_users, route_jobs, route_login

api_router = APIRouter()
api_router.include_router(router=route_users.router, prefix="/user", tags=["users"])
api_router.include_router(router=route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(router=route_login.router, prefix="/login", tags=["login"])
