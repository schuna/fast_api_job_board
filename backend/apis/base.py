from fastapi import APIRouter
from apis.version1 import route_users, route_jobs

api_router = APIRouter()
api_router.include_router(router=route_users.router, prefix="/user", tags=["users"])
api_router.include_router(router=route_jobs.router, prefix="/jobs", tags=["jobs"])
