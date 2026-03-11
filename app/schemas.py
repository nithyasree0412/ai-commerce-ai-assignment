from pydantic import BaseModel
from typing import List

class ProductInput(BaseModel):
    name: str
    description: str
    materials: List[str]