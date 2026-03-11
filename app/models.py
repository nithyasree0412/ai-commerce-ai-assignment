from pydantic import BaseModel
from typing import List, Optional


class ProductInput(BaseModel):
    name: str
    description: str
    materials: List[str]


class ProposalInput(BaseModel):
    budget: int
    event_type: str
    priority: Optional[str] = "sustainable"