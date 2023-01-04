from db.init_db import get_database_client
from fastapi import HTTPException, status

DB_NAME = "dnl_db"

def get_all_catalogue():
    try:
        client = get_database_client()
        db = client[DB_NAME]
        catalogues = db.catalogues
        catalogues = list(catalogues.find(limit=100))  # using pagingation
        client.close()
        return catalogues
    except Exception as e:
        #  use logger to print exception useful in logs
        client.close()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


def get_catalogue_by_manufacturer(manufacturer: str):
    try:
        client = get_database_client()
        db = client[DB_NAME]
        catalogues = db.catalogues
        catalogues = list(catalogues.find({"manufacturer": manufacturer}))  # using pagingation
        
        if catalogues is not None:
            return catalogues
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Catalogue with manufacturer {manufacturer} not found")
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")
