from pydantic import BaseModel


class Catalogue(BaseModel):
    manufacturer: str
    category: str
    model: str
    part: str
    part_category: str
    