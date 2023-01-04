from fastapi import APIRouter
from endpoints.catalogue import catalogue_endpoint

api_router = APIRouter()
api_router.include_router(catalogue_endpoint.router, prefix='/catalogue', tags=['catalogue'])