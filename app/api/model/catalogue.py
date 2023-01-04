from pydantic import BaseModel


class CatalogueBase(BaseModel):
    manufacturer: str
    category: str
    model: str

class Catalogue(CatalogueBase):
    part: str
    part_category: str