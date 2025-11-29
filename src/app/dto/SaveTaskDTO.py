from dataclasses import dataclass
from typing import Optional

@dataclass
class SaveTaskDTO:
    title: int
    end_date: str
    description: Optional[str] = None
    duration: Optional[int] = None
    relevance: Optional[int] = None 
    finnished: Optional[bool] = None
    