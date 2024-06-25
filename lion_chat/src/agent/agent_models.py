from pydantic import BaseModel
from typing import List, Optional

class Agent(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    capabilities: List[str] = []

class Task(BaseModel):
    id: str
    agent_id: str
    description: str
    status: str