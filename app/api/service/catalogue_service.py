from db.init_db import get_database
from fastapi import HTTPException, status


def get_all_catalogue():
    try:
        db = get_database()
        catalogues = db.catalogues
        catalogues = list(catalogues.find(limit=100))  # using pagingation

        return catalogues
    except Exception as e:
        #  use logger to print exception useful in logs
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


def get_catalogue_by_manufacturer(manufacturer: str):
    try:
        db = get_database()
        catalogues = db.catalogues
        catalogues = list(catalogues.find({"manufacturer": manufacturer}))  # using pagingation
        
        if catalogues is not None:
            return catalogues
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Catalogue with manufacturer {manufacturer} not found")
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
