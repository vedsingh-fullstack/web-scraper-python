from typing import Optional, List
from fastapi import APIRouter, status
from fastapi_pagination import Page, add_pagination, paginate
import service.catalogue_service as catalogue_service
from model.catalogue import Catalogue

router = APIRouter()

    

@router.get('/', response_description='Get catalogue list', status_code=status.HTTP_200_OK, response_model=Page[Catalogue])
def get_catalogue(manufacturer: Optional[str] = None):
    if manufacturer is None:
        return paginate(catalogue_service.get_all_catalogue())
    else:
        return paginate(catalogue_service.get_catalogue_by_manufacturer(manufacturer))
